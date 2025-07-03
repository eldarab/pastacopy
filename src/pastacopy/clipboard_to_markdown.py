import pyperclip
from PIL import ImageGrab
import base64
import io


def clipboard_to_markdown() -> str:
    """
    Gets an image from the clipboard, encodes it as a base64 string, and returns a Markdown image tag
    suitable for use in Markdown or Jupyter Notebooks.

    Returns:
        str: A Markdown image tag with the image encoded as a base64 string, or a message if no image is found.
    """
    # Try to get an image from the clipboard
    image = ImageGrab.grabclipboard()
    if image is None:
        return "No image found in clipboard."

    # Convert the image to bytes (PNG format)
    buffered = io.BytesIO()
    image.save(buffered, format="PNG")
    img_bytes = buffered.getvalue()

    # Encode the image bytes to base64
    img_b64 = base64.b64encode(img_bytes).decode('utf-8')

    # Create the Markdown image tag with base64 data
    markdown_img = f'![img](data:image/png;base64,{img_b64})'
    return markdown_img
