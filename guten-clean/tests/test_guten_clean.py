import os
import pytest
from guten_clean import cleaner


@pytest.fixture
def txt_ebook_text():
    with open("C:/Windows/System32/guten-clean/tests/test_data/the_yellow_wallpaper.txt", "r", encoding="utf-8") as f:
        return f.read()


@pytest.fixture
def html_ebook_text():
    with open("C:/Windows/System32/guten-clean/tests/test_data/the_yellow_wallpaper.html", "r", encoding="utf-8") as f:
        return f.read()


def test_clean_txt_ebook(txt_ebook_text):
    cleaned_text = cleaner.clean_ebook(txt_ebook_text)
    assert "The Project Gutenberg eBook" not in cleaned_text
    assert "*** START OF THIS PROJECT GUTENBERG EBOOK" not in cleaned_text
    assert "*** END OF THIS PROJECT GUTENBERG EBOOK" not in cleaned_text
    assert "It is very seldom that mere ordinary people" in cleaned_text
    assert cleaned_text.startswith("It is very seldom")
    assert cleaned_text.endswith("he hates to have me write a word.")


def test_clean_html_ebook(html_ebook_text):
    cleaned_text = cleaner.clean_ebook(html_ebook_text)
    assert "The Project Gutenberg eBook" not in cleaned_text
    assert "*** START OF THIS PROJECT GUTENBERG EBOOK" not in cleaned_text
    assert "*** END OF THIS PROJECT GUTENBERG EBOOK" not in cleaned_text
    assert "It is very seldom that mere ordinary people" in cleaned_text
    assert cleaned_text.startswith("It is very seldom")
    assert cleaned_text.endswith("he hates to have me write a word.")