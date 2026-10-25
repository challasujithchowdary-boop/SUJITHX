"""Read-only system information utilities for SUJITHX."""

import os
import platform
import shutil
import sys
from pathlib import Path


def get_system_info():
    """Return basic computer and Python information."""
    return {
        "computer_name": platform.node() or "Unknown",
        "operating_system": platform.system(),
        "os_release": platform.release(),
        "architecture": platform.machine(),
        "python_version": platform.python_version(),
        "python_executable": sys.executable,
        "current_directory": str(Path.cwd()),
        "cpu_count": os.cpu_count(),
    }


def get_disk_info(path="."):
    """Return storage capacity information for a drive or folder."""
    target = Path(path).expanduser()

    if not target.exists():
        raise FileNotFoundError(f"Path not found: {target}")

    usage = shutil.disk_usage(target.resolve())

    return {
        "path": str(target.resolve()),
        "total_bytes": usage.total,
        "used_bytes": usage.used,
        "free_bytes": usage.free,
        "total_gb": round(usage.total / (1024 ** 3), 2),
        "used_gb": round(usage.used / (1024 ** 3), 2),
        "free_gb": round(usage.free / (1024 ** 3), 2),
    }


def display_system_info():
    """Print system information in a readable format."""
    print("\n=== SUJITHX SYSTEM INFORMATION ===")

    for key, value in get_system_info().items():
        print(f"{key.replace('_', ' ').title()}: {value}")

    print("\n=== DISK INFORMATION ===")

    try:
        for key, value in get_disk_info().items():
            print(f"{key.replace('_', ' ').title()}: {value}")
    except OSError as exc:
        print(f"Could not read disk information: {exc}")