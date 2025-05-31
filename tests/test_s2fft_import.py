import importlib
import pytest

def test_can_import_s2fft():
    try:
        importlib.import_module("s2fft")
    except Exception as exc:
        pytest.fail(f"Could not import s2fft: {exc}")

