"""
SUJITHX - The Ultimate Python Toolkit
"""

_version_ = "0.1.0"
_author_ = "Sujith"


def hello(name="Developer"):
    """Return a personalized greeting."""
    return f"Hello, {name}! Welcome to SUJITHX."


def add(a, b):
    """Add two numbers."""
    return a + b


def multiply(a, b):
    """Multiply two numbers."""
    return a * b


def percentage(value, total):
    """Calculate a percentage safely."""
    if total == 0:
        raise ValueError("Total cannot be zero.")

    return (value / total) * 100
from .files import (
    search_files,
    analyze_folder,
    find_duplicates,
    largest_files,
    format_bytes,
)
from .security import (
    sha256_text,
    sha256_file,
    generate_token,
    generate_password,
    check_password_strength,
)
from .colors import (
    color_text,
    success,
    error,
    warning,
    info,
    banner,
    progress_bar,
    print_progress,
)
from .logger import (
    create_logger,
    log_info,
    log_warning,
    log_error,
    log_debug,
)
from .automation import (
    ensure_directory,
    list_files,
    get_file_info,
    copy_file,
    read_text,
    write_text,
    file_exists,
)
from .system_info import (
    get_system_info,
    get_disk_info,
    display_system_info,
)
from .network import (
    get_hostname,
    get_local_ip,
    check_internet,
    get_network_info,
)