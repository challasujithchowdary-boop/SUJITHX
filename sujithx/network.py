"""Basic, read-only network utilities for SUJITHX."""

import socket
import urllib.error
import urllib.request


def get_hostname():
    """Return this computer's hostname."""
    return socket.gethostname()


def get_local_ip():
    """Return the local IP address when available."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
            sock.connect(("192.0.2.1", 80))
            return sock.getsockname()[0]
    except OSError:
        return "Unavailable"


def check_internet(timeout=3):
    """Check whether an HTTPS connection can be established."""
    try:
        request = urllib.request.Request(
            "https://www.google.com/generate_204",
            method="GET",
        )
        with urllib.request.urlopen(request, timeout=timeout) as response:
            return response.status in (200, 204)
    except (OSError, urllib.error.URLError, TimeoutError):
        return False


def get_network_info():
    """Return basic network information."""
    return {
        "hostname": get_hostname(),
        "local_ip": get_local_ip(),
        "internet_available": check_internet(),
    }