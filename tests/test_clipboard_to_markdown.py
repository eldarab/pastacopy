import pytest
from pastacopy.clipboard_to_markdown import clipboard_to_markdown


# ---- fixtures --------------------------------------------------------------
@pytest.fixture
def empty_clip(monkeypatch):
    """Simulate a clipboard with no image or text."""
    monkeypatch.setattr("PIL.ImageGrab.grabclipboard", lambda: None)
    monkeypatch.setattr("pyperclip.paste", lambda: "")


@pytest.fixture
def png_clip(tmp_path, monkeypatch):
    """Simulate a clipboard containing a PNG file path."""
    from PIL import Image

    img = tmp_path / "dummy.png"
    Image.new("RGB", (1, 1)).save(img)
    monkeypatch.setattr("PIL.ImageGrab.grabclipboard", lambda: str(img))
    monkeypatch.setattr("pyperclip.paste", lambda: "")
    return img


# ---- unit tests ------------------------------------------------------------
def test_no_image_returns_msg(empty_clip):
    assert clipboard_to_markdown() == "No image found in clipboard."


def test_png_clip_returns_md_link(png_clip):
    md = clipboard_to_markdown()
    assert md.endswith(f"![]({png_clip.name})")
