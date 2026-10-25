"""Terminal styling utilities for SUJITHX."""

import shutil
import sys


RESET = "\033[0m"
BOLD = "\033[1m"

COLORS = {
    "black": "\033[30m",
    "red": "\033[31m",
    "green": "\033[32m",
    "yellow": "\033[33m",
    "blue": "\033[34m",
    "magenta": "\033[35m",
    "cyan": "\033[36m",
    "white": "\033[37m",
}


def color_text(text, color="cyan", bold=False):
    """Return text with ANSI terminal colors."""
    if color not in COLORS:
        raise ValueError(f"Unsupported color: {color}")

    style = COLORS[color]
    if bold:
        style += BOLD

    return f"{style}{text}{RESET}"


def success(message):
    """Format a success message."""
    return color_text(f"[SUCCESS] {message}", "green", True)


def error(message):
    """Format an error message."""
    return color_text(f"[ERROR] {message}", "red", True)


def warning(message):
    """Format a warning message."""
    return color_text(f"[WARNING] {message}", "yellow", True)


def info(message):
    """Format an information message."""
    return color_text(f"[INFO] {message}", "cyan")


def banner(title="SUJITHX"):
    """Create a centered terminal banner."""
    width = max(40, min(shutil.get_terminal_size((80, 20)).columns, 100))
    border = "=" * width
    heading = f" {title} ".center(width, "=")

    return (
        color_text(border, "magenta", True)
        + "\n"
        + color_text(heading, "cyan", True)
        + "\n"
        + color_text(border, "magenta", True)
    )


def progress_bar(percent, width=30):
    """Display a simple text progress bar."""
    if not 0 <= percent <= 100:
        raise ValueError("percent must be between 0 and 100")

    if width < 1:
        raise ValueError("width must be at least 1")

    filled = round(width * percent / 100)
    bar = "#" * filled + "-" * (width - filled)

    return f"[{bar}] {percent:.1f}%"


def print_progress(percent, width=30):
    """Print a progress bar on the terminal."""
    print(progress_bar(percent, width), file=sys.stdout)