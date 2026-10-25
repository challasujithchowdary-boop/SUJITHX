"""Safe file and folder automation utilities for SUJITHX."""

from pathlib import Path
import shutil


def ensure_directory(folder):
    """Create a folder if it does not already exist."""
    path = Path(folder).expanduser()
    path.mkdir(parents=True, exist_ok=True)
    return str(path.resolve())


def list_files(folder, pattern="*"):
    """List files inside a folder and its subfolders."""
    root = Path(folder).expanduser()

    if not root.is_dir():
        raise NotADirectoryError(f"Folder not found: {root}")

    return sorted(
        (str(path) for path in root.rglob(pattern) if path.is_file()),
        key=str.lower,
    )


def get_file_info(file_path):
    """Return basic information about a file."""
    path = Path(file_path).expanduser()

    if not path.is_file():
        raise FileNotFoundError(f"File not found: {path}")

    details = path.stat()

    return {
        "name": path.name,
        "path": str(path.resolve()),
        "extension": path.suffix.lower(),
        "size_bytes": details.st_size,
        "size_kb": round(details.st_size / 1024, 2),
    }


def copy_file(source, destination, overwrite=False):
    """Copy a file without overwriting an existing file by default."""
    source_path = Path(source).expanduser()
    destination_path = Path(destination).expanduser()

    if not source_path.is_file():
        raise FileNotFoundError(f"Source file not found: {source_path}")

    if destination_path.exists() and not overwrite:
        raise FileExistsError(
            f"Destination already exists: {destination_path}"
        )

    destination_path.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source_path, destination_path)

    return str(destination_path.resolve())


def read_text(file_path, encoding="utf-8"):
    """Read a UTF-8 text file."""
    path = Path(file_path).expanduser()

    if not path.is_file():
        raise FileNotFoundError(f"File not found: {path}")

    return path.read_text(encoding=encoding)


def write_text(file_path, content, overwrite=False, encoding="utf-8"):
    """Write a text file, refusing to overwrite by default."""
    path = Path(file_path).expanduser()

    if path.exists() and not overwrite:
        raise FileExistsError(
            f"File already exists: {path}. Set overwrite=True to replace it."
        )

    path.parent.mkdir(parents=True, exist_ok=True)

    if overwrite:
        path.write_text(content, encoding=encoding)
    else:
        with path.open("x", encoding=encoding) as file:
            file.write(content)

    return str(path.resolve())


def file_exists(file_path):
    """Check whether a file exists."""
    return Path(file_path).expanduser().is_file()