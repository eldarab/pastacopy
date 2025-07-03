import pyperclip

def clipboard_to_markdown() -> str:
    """
    Converts the content of the clipboard to a Markdown formatted string.
    
    Returns:
        str: The content of the clipboard formatted as Markdown.
    """

    # Get the text from the clipboard
    clipboard_text = pyperclip.paste()

    # Convert the text to Markdown format
    markdown_text = f"```\n{clipboard_text}\n```"

    return markdown_text
