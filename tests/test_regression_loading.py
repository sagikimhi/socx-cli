from __future__ import annotations

from textwrap import dedent
from collections import OrderedDict

from socx.regression import Regression, Test as RegressionTest


def test_regression_preserves_explicit_test_map() -> None:
    tests = [
        RegressionTest(name="alpha", command="echo alpha"),
        RegressionTest(name="beta", command="echo beta"),
    ]

    regression = Regression(
        name="smoke",
        test_map=OrderedDict((test.id, test) for test in tests),
    )

    assert regression.tests == tests
    assert list(regression.test_map.values()) == tests


def test_regression_from_file_returns_single_regression(tmp_path) -> None:
    path = tmp_path / "single.yaml"
    path.write_text(
        dedent(
            """
            smoke:
              - name: alpha
                exec: echo alpha
              - name: beta
                exec: echo beta
            """.strip()
        )
    )

    regression = Regression.from_file(path)

    assert regression.name == "single"
    assert [test.name for test in regression.tests] == ["smoke"]
    regressions = [
        sub_regression
        for sub_regression in regression.tests
        if isinstance(sub_regression, Regression)
    ]
    assert [
        test.name
        for sub_regression in regressions
        for test in sub_regression.tests
    ] == [
        "alpha",
        "beta",
    ]
    assert "echo alpha" in str(regressions[0].tests[0].exec)
    assert "echo beta" in str(regressions[0].tests[1].exec)


def test_regression_from_file_returns_parent_regression(tmp_path) -> None:
    path = tmp_path / "multi.yaml"
    path.write_text(
        dedent(
            """
            smoke:
              - name: alpha
                exec: echo alpha
            nightly:
              - name: beta
                exec: echo beta
            """
        )
    )

    regression = Regression.from_file(path)

    assert regression.name == "multi"
    assert all(isinstance(test, Regression) for test in regression.tests)
    assert [child.name for child in regression.tests] == [
        "smoke",
        "nightly",
    ]
    assert [test.name for test in regression.tests[0].tests] == ["alpha"]
    assert [test.name for test in regression.tests[1].tests] == ["beta"]


def test_regression_from_file_expands_test_count(tmp_path) -> None:
    path = tmp_path / "counted.yaml"
    path.write_text(
        dedent(
            """
            smoke:
              - name: alpha
                exec: echo alpha
                count: 3
            """
        )
    )

    regression = Regression.from_file(path)
    smoke = regression.tests[0]

    assert isinstance(smoke, Regression)
    assert [test.name for test in smoke.tests] == [
        "alpha_run_1",
        "alpha_run_2",
        "alpha_run_3",
    ]
    assert all("echo alpha" in str(test.exec) for test in smoke.tests)


def test_regression_loader_renders_file_with_context(tmp_path) -> None:
    path = tmp_path / "generated.yaml"
    path.write_text(
        dedent(
            """
            context:
              count: 2
              seeds: [0, random]
              run_dir: /tmp/regression/runs
              build_dir: /tmp/regression/build
              exec: |
                socrun --compile_once \\
                    --compiledir {{ build_dir }} \\
                    --rundir {{ run_dir }}/run_{{ index }} \\
                    --test {{ name }}.cfg \\
                    --seed {{ seed }}
              test_names:
                - foo
                - bar
                - bazz

            my_regression:
              tests:
                - name: foobarbazz_test
                  seed: [1, 2, 3]
                  count: 3
                {% for name in test_names %}
                - name: {{ name }}_test
                {% endfor %}
            """
        )
    )

    regression = Regression.from_file(path)
    my_regression = regression.tests[0]

    assert isinstance(my_regression, Regression)
    assert [test.name for test in my_regression.tests] == [
        "foobarbazz_test_run_1",
        "foobarbazz_test_run_2",
        "foobarbazz_test_run_3",
        "foo_test_run_1",
        "foo_test_run_2",
        "bar_test_run_1",
        "bar_test_run_2",
        "bazz_test_run_1",
        "bazz_test_run_2",
    ]

    first = str(my_regression.tests[0].exec)
    assert "--compiledir /tmp/regression/build" in first
    assert "--rundir /tmp/regression/runs/run_0" in first
    assert "--test foobarbazz_test.cfg" in first
    assert "--seed 1" in first

    repeated = str(my_regression.tests[4].exec)
    assert "--rundir /tmp/regression/runs/run_1" in repeated
    assert "--test foo_test.cfg" in repeated
    assert "--seed random" in repeated


def test_regression_loader_supports_regression_defaults(tmp_path) -> None:
    path = tmp_path / "defaults.yaml"
    path.write_text(
        dedent(
            """
            smoke:
              defaults:
                count: 2
                seed: [11, 22]
                exec: echo {{ name }} {{ index }} {{ seed }}
              tests:
                - name: alpha
                - name: beta
                  count: 1
                  seed: 33
            """
        )
    )

    regression = Regression.from_file(path)
    smoke = regression.tests[0]

    assert isinstance(smoke, Regression)
    assert [test.name for test in smoke.tests] == [
        "alpha_run_1",
        "alpha_run_2",
        "beta",
    ]
    assert "echo alpha 0 11" in str(smoke.tests[0].exec)
    assert "echo alpha 1 22" in str(smoke.tests[1].exec)
    assert "echo beta 0 33" in str(smoke.tests[2].exec)
