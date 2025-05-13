import logging
import sys
from typing import Literal


class Logger(logging.Logger):
    """Handles logging to the file and stroudt with timestamps."""

    def __init__(
        self,
        name: str,
        level: Literal["DEBUG", "INFO", "WARNING", "ERROR"] = "DEBUG",
    ):
        super().__init__(name)
        self.setLevel(level)
        self.stdout_handler = logging.StreamHandler(sys.stdout)
        formatter = "%(name)s | %(levelname)s | %(asctime)s | %(message)s"
        self.fmt = formatter
        self.stdout_handler.setFormatter(logging.Formatter(formatter))
        self.addHandler(self.stdout_handler)
