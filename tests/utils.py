from __future__ import annotations

from time import perf_counter
import asyncio


async def wait_for(predicate, max_wait: float = 3.0) -> None:
    deadline = perf_counter() + max_wait
    while perf_counter() < deadline:
        if predicate():
            return
        await asyncio.sleep(0.25)
    msg = "Condition was not met before timeout."
    raise AssertionError(msg)
