from dataclasses import dataclass
from socx import UIDMixin
from socx import console


@dataclass
class UIDTest(UIDMixin):
    iteration: int


def test() -> None:
    inst_ = UIDTest(0)
    for _ in range(1, 999):
        inst = UIDTest(_)
        assert inst.iteration == inst.uid
        console.print(UIDTest.dref(inst.ref))
        del inst
        console.print(UIDTest.dref(_))

    console.print(UIDTest.dref(inst_.ref))
    del inst_
    console.print(UIDTest.dref(0))


if __name__ == "__main__":
    test()
