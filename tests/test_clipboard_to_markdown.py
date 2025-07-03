import pytest
from pastacopy.clipboard_to_markdown import clipboard_to_markdown


@pytest.fixture
def empty_clip(monkeypatch):
    """Simulate a clipboard with no image or text."""
    monkeypatch.setattr("PIL.ImageGrab.grabclipboard", lambda: None)


def test_no_image_returns_msg(empty_clip):
    assert clipboard_to_markdown() == "No image found in clipboard."
