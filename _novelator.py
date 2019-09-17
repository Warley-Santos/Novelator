import requests
from bs4 import BeautifulSoup
from ebooklib import epub

import chapters_utils, links, string_utils

def generate_ebook():

    novel_link = links.btth
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
    # for i in range(0, 3):
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
    style = 'BODY {color: white;}'
    nav_css = epub.EpubItem(uid="style_nav", file_name="style/nav.css", media_type="text/css", content=style)

    # add CSS file
    book.add_item(nav_css)

    for i in range(0, len(chapter_title)):
        book.toc.append((epub.Link(chapter_title[i].text + '.xhtml', chapter_title[i].text, "chapter" + str(i+1) )))

    # basic spine
    book.spine = ['nav']

    for i in range(0, len(book_chapters)):
        book.spine.append(book_chapters[i])

    book.add_item(epub.EpubNcx())
    book.add_item(epub.EpubNav())

    # save in books folder
    epub.write_epub('books/btth.epub', book, {})

generate_ebook()
