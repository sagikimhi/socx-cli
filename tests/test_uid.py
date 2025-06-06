from dataclasses import dataclass
import gc

from socx import UIDMixin


@dataclass
class UIDTest(UIDMixin):
    iteration: int


def test_uid_increments_and_deref() -> None:
    first = UIDTest(0)
    assert first.uid == 0
    assert UIDTest.dref(first.ref) is first

    for i in range(1, 5):
        inst = UIDTest(i)
        assert inst.uid == i
        assert UIDTest.dref(inst.ref) is inst
        ref = inst.ref
        del inst
        gc.collect()
        assert UIDTest.dref(ref) is None

    ref_first = first.ref
    del first
    gc.collect()
    assert UIDTest.dref(ref_first) is None
