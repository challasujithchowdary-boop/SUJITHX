"""Basic automated tests for SUJITHX."""

import unittest
import tempfile
from pathlib import Path

import sujithx


class TestSUJITHX(unittest.TestCase):

    def test_hello(self):
        self.assertIn("Sujith", sujithx.hello("Sujith"))

    def test_add(self):
        self.assertEqual(sujithx.add(5, 3), 8)

    def test_multiply(self):
        self.assertEqual(sujithx.multiply(4, 3), 12)

    def test_percentage(self):
        self.assertEqual(sujithx.percentage(25, 100), 25.0)

    def test_percentage_zero_total(self):
        with self.assertRaises(ValueError):
            sujithx.percentage(10, 0)

    def test_token_generation(self):
        token = sujithx.generate_token()
        self.assertEqual(len(token), 32)

    def test_password_generation(self):
        password = sujithx.generate_password()
        self.assertGreaterEqual(len(password), 12)

    def test_file_automation(self):
        with tempfile.TemporaryDirectory() as temporary:
            folder = Path(temporary)
            file_path = folder / "hello.txt"

            sujithx.write_text(str(file_path), "SUJITHX works!")

            self.assertTrue(sujithx.file_exists(str(file_path)))
            self.assertEqual(
                sujithx.read_text(str(file_path)),
                "SUJITHX works!",
            )

    def test_file_info(self):
        with tempfile.TemporaryDirectory() as temporary:
            file_path = Path(temporary) / "sample.txt"
            file_path.write_text("Hello", encoding="utf-8")

            info = sujithx.get_file_info(str(file_path))

            self.assertEqual(info["name"], "sample.txt")
            self.assertEqual(info["size_bytes"], 5)

    def test_format_bytes(self):
        self.assertEqual(sujithx.format_bytes(1024), "1.00 KB")


if __name__ == "__main__":
    unittest.main()