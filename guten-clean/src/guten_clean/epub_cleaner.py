
import ebooklib
from ebooklib import epub
from bs4 import BeautifulSoup
from . import cleaner

def clean_epub(input_path, output_path):
    book = epub.read_epub(input_path)
    new_book = epub.EpubBook()
    new_book.set_identifier(book.uid)
    new_book.set_title(book.title)
    new_book.set_language(book.language)

    full_text = []

    for item in book.get_items_of_type(ebooklib.ITEM_DOCUMENT):
        soup = BeautifulSoup(item.get_content(), 'html.parser')
        full_text.append(soup.get_text())

    full_text = "\n".join(full_text)
    cleaned_text = cleaner.clean_ebook(full_text)

    # Create a new chapter with the cleaned text
    c1 = epub.EpubHtml(title='Cleaned Content', file_name='chap_1.xhtml', lang='en')
    c1.content = f'<html><head></head><body><p>{cleaned_text.replace("\n", "<br>")}</p></body></html>'
    new_book.add_item(c1)

    # Add default NCX and Nav files
    new_book.add_item(epub.EpubNcx())
    new_book.add_item(epub.EpubNav())

    # Define the book spine
    new_book.spine = ['nav', c1]

    epub.write_epub(output_path, new_book, {})
