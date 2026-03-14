from __future__ import annotations

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
        """
regressions:
  smoke:
    - name: alpha
      exec: echo alpha
    - name: beta
      exec: echo beta
""".strip()
    )

    regression = Regression.from_file(path)

    assert regression.name == "smoke"
    assert [test.name for test in regression.tests] == ["alpha", "beta"]
    assert "echo alpha" in str(regression.tests[0].exec)
    assert "echo beta" in str(regression.tests[1].exec)


def test_regression_from_file_returns_parent_regression(tmp_path) -> None:
    path = tmp_path / "multi.yaml"
    path.write_text(
        """
regressions:
  smoke:
    - name: alpha
      exec: echo alpha
  nightly:
    - name: beta
      exec: echo beta
""".strip()
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
