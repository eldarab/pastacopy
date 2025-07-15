import pytest
from pastacopy import clipboard_to_markdown


@pytest.fixture
def empty_clip(monkeypatch):
    """Simulate an empty clipboard (no image present)."""
    monkeypatch.setattr("PIL.ImageGrab.grabclipboard", lambda: None)


def test_no_image_raises_value_error(empty_clip):
    """The helper should raise ValueError when the clipboard has no image."""
    with pytest.raises(ValueError, match="Clipboard does not contain an image."):
        clipboard_to_markdown()
