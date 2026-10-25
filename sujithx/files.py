"""File intelligence utilities for SUJITHX."""

from pathlib import Path
from collections import Counter
import hashlib


def search_files(folder, pattern="*"):
    """Search for files recursively."""
    root = Path(folder).expanduser()

    if not root.is_dir():
        raise NotADirectoryError(f"Folder not found: {root}")

    return sorted(
        (p for p in root.rglob(pattern) if p.is_file()),
        key=lambda p: str(p).lower()
    )


def analyze_folder(folder):
    """Analyze files and folders."""
    root = Path(folder).expanduser()

    if not root.is_dir():
        raise NotADirectoryError(f"Folder not found: {root}")

    files = [p for p in root.rglob("*") if p.is_file()]
    extensions = Counter(
        p.suffix.lower() or "[no extension]" for p in files
    )

    total_bytes = 0

    for path in files:
        try:
            total_bytes += path.stat().st_size
        except OSError:
            pass

    return {
        "folder": str(root.resolve()),
        "file_count": len(files),
        "total_bytes": total_bytes,
        "total_mb": round(total_bytes / (1024 * 1024), 2),
        "extensions": dict(extensions),
    }


def find_duplicates(folder):
    """Find duplicate files using SHA-256 hashes."""
    root = Path(folder).expanduser()

    if not root.is_dir():
        raise NotADirectoryError(f"Folder not found: {root}")

    hashes = {}

    for path in root.rglob("*"):
        if not path.is_file():
            continue

        try:
            digest = hashlib.sha256()

            with path.open("rb") as file:
                for chunk in iter(lambda: file.read(1024 * 1024), b""):
                    digest.update(chunk)

            hashes.setdefault(digest.hexdigest(), []).append(str(path))

        except OSError:
            continue

    return [paths for paths in hashes.values() if len(paths) > 1]


def largest_files(folder, limit=10):
    """Find the largest files."""
    if limit < 1:
        raise ValueError("limit must be at least 1")

    root = Path(folder).expanduser()

    if not root.is_dir():
        raise NotADirectoryError(f"Folder not found: {root}")

    files = []

    for path in root.rglob("*"):
        try:
            if path.is_file():
                files.append((str(path), path.stat().st_size))
        except OSError:
            continue

    return sorted(files, key=lambda item: item[1], reverse=True)[:limit]


def format_bytes(size):
    """Convert bytes to a readable size."""
    if size < 0:
        raise ValueError("size cannot be negative")

    for unit in ("B", "KB", "MB", "GB", "TB"):
        if size < 1024 or unit == "TB":
            return f"{size:.2f} {unit}"
        size /= 1024