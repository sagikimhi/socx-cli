import logging

from socx.io.log import Level, set_level


def test_set_level_updates_logger_and_handlers() -> None:
    logger = logging.Logger("socx.test.logging")
    handler_a = logging.StreamHandler()
    handler_b = logging.StreamHandler()

    handler_a.setLevel(Level.FATAL)
    handler_b.setLevel(Level.ERROR)
    logger.addHandler(handler_a)
    logger.addHandler(handler_b)

    set_level(Level.DEBUG, logger_=logger)

    assert logger.level == Level.DEBUG
    assert handler_a.level == Level.DEBUG
    assert handler_b.level == Level.DEBUG
