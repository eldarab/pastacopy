from PIL import ImageGrab
import base64
import io


def clipboard_to_markdown() -> str:
    """
    Converts an image from the clipboard into a Markdown image tag with embedded base64 data.

    Returns:
        str: A Markdown image tag with the image encoded as base64, or an error message.

    Raises:
        ValueError: If the clipboard does not contain an image.
    """
    image = ImageGrab.grabclipboard()
    if not isinstance(image, ImageGrab.Image.Image):
        raise ValueError("Clipboard does not contain an image.")

    buffered = io.BytesIO()
    image.save(buffered, format="PNG")
    img_b64 = base64.b64encode(buffered.getvalue()).decode("utf-8")
    return f"![img](data:image/png;base64,{img_b64})"
