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
