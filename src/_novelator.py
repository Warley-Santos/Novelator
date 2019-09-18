import requests
from bs4 import BeautifulSoup
from ebooklib import epub

import book_utils
import chapters_utils
import links
import string_utils

def generate_ebook():

    novel_link = links.svnk
    chapter_contents = ""
    
    chapter_title = []
    book_chapters = []

    book = epub.EpubBook()

    # add metadata
    book.set_identifier('btth')
    book.set_title('Battle Through the Heavens')
    book.set_language('en')

    book.add_author('Heavenly Silkworm Potato')

    chapter_list = chapters_utils.get_chapters_list("https://www.wuxiaworld.com" + novel_link)

    for i, c in enumerate(chapter_list):
        print("Getting: " + "https://www.wuxiaworld.com" + c.link) 

        response = requests.get("https://www.wuxiaworld.com" + c.link)
        soup = BeautifulSoup(response.text,"html.parser")

        chapter_title.append(chapters_utils.get_chapter_title(soup))

        chapter_contents = chapters_utils.get_chapter_contents(soup)
        chapter_contents = string_utils.replace_odd_chars(chapter_contents)

        book_chapters.append(epub.EpubHtml(title=chapter_title[i].text, file_name=chapter_title[i].text + '.xhtml', lang='en'))

        book_chapters[i].content = chapter_contents
        chapter_contents = ""

        book.add_item(book_chapters[i])

    # define CSS style
    book = book_utils.add_css(book)

    book = book_utils.generate_sumary(chapter_title, book)
    book = book_utils.add_spine(book)
    book = book_utils.append_chapters(book_chapters, book)
    book = book_utils.add_nav_ncx(book)

    # save in books folder
    epub.write_epub('books/teste.epub', book, {})

generate_ebook()
