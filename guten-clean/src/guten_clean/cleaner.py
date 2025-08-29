import re

def clean_ebook(text):
    """Clean an ebook text by removing the Project Gutenberg boilerplate."""
    text = remove_gutenberg_boilerplate(text)
    text = remove_copyright_and_notes(text)
    return text

def remove_copyright_and_notes(text):
    """Remove copyright, editor's notes, and other preamble from the text."""
    # List of regex patterns that often mark the end of the preamble.
    # We will find the last occurrence of any of these.
    end_of_preamble_markers = [
        r"All rights reserved",
        r"PRINTED IN THE UNITED STATES OF AMERICA",
        r"ISBN \d{1,}-\d{1,}-\d{1,}-\d{1,}-\d{1,}",
        r"This book is a work of fiction.",
        r"[\d\s]+printing", # e.g., "Twenty-third printing"
    ]

    last_marker_pos = -1

    for marker in end_of_preamble_markers:
        # Find all matches for the current marker
        matches = list(re.finditer(marker, text, re.IGNORECASE))
        if matches:
            # Get the end position of the last match
            last_pos = matches[-1].end()
            if last_pos > last_marker_pos:
                last_marker_pos = last_pos

    if last_marker_pos != -1:
        # Find the end of the line containing the last marker
        end_of_line_pos = text.find('\n', last_marker_pos)
        if end_of_line_pos != -1:
            # Return everything after that line, stripping leading whitespace
            return text[end_of_line_pos:].lstrip()

    # If no markers were found, return the text as is.
    return text

def remove_gutenberg_boilerplate(text):
    """Remove the Project Gutenberg header and footer."""
    start_marker_regex = r"\*\*\*\s*START OF (THIS|THE) PROJECT GUTENBERG EBOOK.*\*\*\*"
    end_marker_regex = r"\*\*\*\s*END OF (THIS|THE) PROJECT GUTENBERG EBOOK.*\*\*\*"

    # Find the start marker and slice the text after it
    start_match = re.search(start_marker_regex, text, re.IGNORECASE)
    if start_match:
        text = text[start_match.end():]

    # Find the end marker and slice the text before it
    end_match = re.search(end_marker_regex, text, re.IGNORECASE)
    if end_match:
        text = text[:end_match.start()]

    return text
