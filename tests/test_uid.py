from dataclasses import dataclass
from socx import UIDMixin


@dataclass
class UIDTest(UIDMixin):
    pass


def test() -> None:
    for i in range(0, 10):
        inst = UIDTest()
        assert i == inst.uid

    inst = UIDTest()
    ref = inst.ref

    assert UIDTest.dref(ref) is inst
    del inst
    assert UIDTest.dref(ref) is None


if __name__ == "__main__":
    test()
