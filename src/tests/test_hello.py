import pytest

from core.utils.palette import google_text


def test_hello():
    assert "hello" == "hello"


def test_google_text():
    try:
        google_text()
    except Exception as e:
        pytest.fail(f"{e}")
