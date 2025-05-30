import pathlib
import sys
import pytest


def test_s2fft_extension_matches_python():
    try:
        import s2fft_lib
    except Exception as exc:
        pytest.skip(f"s2fft_lib not available: {exc}")
    libs = list(pathlib.Path(s2fft_lib.__path__[0]).glob("_s2fft*.so"))
    assert libs, "_s2fft extension missing"
    fname = libs[0].name
    expected_tag = f"cpython-{sys.version_info.major}{sys.version_info.minor}"
    assert expected_tag in fname, (
        f"Extension built for different Python version: {fname}, expected {expected_tag}")

