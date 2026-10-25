"""Professional logging utilities for SUJITHX."""

import logging
from pathlib import Path


def create_logger(
    name="SUJITHX",
    log_file="sujithx.log",
    level="INFO",
):
    """Create a logger that writes to both console and file."""

    valid_levels = {
        "DEBUG": logging.DEBUG,
        "INFO": logging.INFO,
        "WARNING": logging.WARNING,
        "ERROR": logging.ERROR,
        "CRITICAL": logging.CRITICAL,
    }

    level_name = level.upper()

    if level_name not in valid_levels:
        raise ValueError(
            "level must be DEBUG, INFO, WARNING, ERROR, or CRITICAL"
        )

    logger = logging.getLogger(name)
    logger.setLevel(valid_levels[level_name])
    logger.propagate = False

    # Avoid adding duplicate handlers when called repeatedly.
    if logger.handlers:
        return logger

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    console_handler = logging.StreamHandler()
    console_handler.setLevel(valid_levels[level_name])
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    if log_file:
        path = Path(log_file).expanduser()
        path.parent.mkdir(parents=True, exist_ok=True)

        file_handler = logging.FileHandler(
            path,
            encoding="utf-8",
        )
        file_handler.setLevel(valid_levels[level_name])
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger


def log_info(message, logger=None):
    """Log an informational message."""
    (logger or create_logger()).info(message)


def log_warning(message, logger=None):
    """Log a warning message."""
    (logger or create_logger()).warning(message)


def log_error(message, logger=None):
    """Log an error message."""
    (logger or create_logger()).error(message)


def log_debug(message, logger=None):
    """Log a debug message."""
    (logger or create_logger(level="DEBUG")).debug(message)