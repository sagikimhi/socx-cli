from __future__ import annotations

import logging
from typing import override

from socx import Test, TestResult

from socx_plugins.rgr.post_process_sim_log import TestResults


logger = logging.getLogger(__name__)


class PixieTest(Test):
    @override
    def _parse_result(self) -> TestResult:
        if self.returncode != 0:
            return TestResult.Failed

        run_log = self.runtime_logs / self.name / "logs" / "run.log"
        logger.debug(f"parsing result from file: '{run_log}'")

        result_parser = TestResults()
        result_parser.reset_log(run_log)
        result_parser.parse_log()
        result_str = result_parser.result

        match result_str:
            case "PASS":
                return TestResult.Passed
            case "FAIL":
                return TestResult.Failed
            case _:
                err = (
                    "Test result could not be determined: Expected 'PASS' or "
                    f"'FAIL', but got '{result_str}'"
                )
                raise ValueError(err)
