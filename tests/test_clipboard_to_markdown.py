import pytest
from src.pastacopy.clipboard_to_markdown import clipboard_to_markdown


def test_clipboard_to_markdown_no_image(no_image_clipboard):
    result = clipboard_to_markdown()
    assert result == "No image found in clipboard."

# Additional tests for image in clipboard would require integration or system tests.
