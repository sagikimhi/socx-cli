from collections.abc import Iterable

from socx.regression.test import Test


def _duplicates(tests: Iterable[Test]) -> Iterable[Test]:
    rv = list()
    seen = set()
    for x in tests:
        if x in seen:
            rv.append(x)
        else:
            seen.add(x)
    return rv


def _warn_duplicates(
    ntests: int, nunique: int, duplicates: Iterable[Test]
) -> None:
    error = f"""
    Note that as a set, the total number of tests in the regression
    has less tests than what the original input list of tests included.
    (i.e. some hashes of the tests were found to be duplicates).

    The original number of tests was: {ntests}.
    The total number of unique tests is: {nunique}.
    The suspected duplicate values are: {duplicates}.
    """
    raise ValueError(error)


def validate_test_list(tests: Iterable[Test]) -> None:
    dups = _duplicates(tests)
    unique = set(tests)
    ntests, nunique = len(tuple(tests)), len(tuple(unique))
    if ntests < nunique:
        _warn_duplicates(ntests, nunique, dups)
