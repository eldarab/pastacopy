import pytest

@pytest.fixture
def no_image_clipboard(monkeypatch):
    import src.pastacopy.clipboard_to_markdown as mod
    monkeypatch.setattr(mod.ImageGrab, "grabclipboard", lambda: None)
    yield
