"""Security utilities for the SUJITHX Python toolkit."""

import hashlib
import secrets
import string
from pathlib import Path


def sha256_text(text):
    """Return the SHA-256 hash of text."""
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def sha256_file(file_path):
    """Calculate a file's SHA-256 hash."""
    digest = hashlib.sha256()

    with Path(file_path).open("rb") as file:
        for chunk in iter(lambda: file.read(1024 * 1024), b""):
            digest.update(chunk)

    return digest.hexdigest()


def generate_token(length=32):
    """Generate a cryptographically secure hexadecimal token."""
    if length < 16:
        raise ValueError("Token length must be at least 16 characters.")

    return secrets.token_hex((length + 1) // 2)[:length]


def generate_password(length=16):
    """Generate a secure password with varied character types."""
    if length < 12:
        raise ValueError("Password length must be at least 12.")

    groups = [
        string.ascii_lowercase,
        string.ascii_uppercase,
        string.digits,
        "!@#$%^&*()-_=+",
    ]

    # Guarantee at least one character from each group.
    password = [secrets.choice(group) for group in groups]
    alphabet = "".join(groups)

    password.extend(
        secrets.choice(alphabet) for _ in range(length - len(password))
    )

    # Securely shuffle the password characters.
    secrets.SystemRandom().shuffle(password)

    return "".join(password)


def check_password_strength(password):
    """Provide a basic password-strength assessment."""
    if not isinstance(password, str):
        raise TypeError("Password must be a string.")

    checks = {
        "length": len(password) >= 12,
        "lowercase": any(c.islower() for c in password),
        "uppercase": any(c.isupper() for c in password),
        "digit": any(c.isdigit() for c in password),
        "symbol": any(not c.isalnum() for c in password),
    }

    score = sum(checks.values())

    if score <= 2:
        rating = "Weak"
    elif score <= 4:
        rating = "Moderate"
    else:
        rating = "Strong"

    return {
        "rating": rating,
        "score": score,
        "checks": checks,
    }