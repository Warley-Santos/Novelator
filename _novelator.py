import requests
from bs4 import BeautifulSoup
from ebooklib import epub

import chapter, links, string_utils

def generate_ebook():

    asdf=""
    url = links.btth
    chapter_contents = ""
    
    chapter_title = []
    chapter_list = []

    book = epub.EpubBook()

    # add metadata
    book.set_identifier('btth')
    book.set_title('Battle Through the Heavens')
    book.set_language('en')

    book.add_author('Heavenly Silkworm Potato')

    for i in range(0, 3):
        print("Getting: " + url+str(i+1))

        response = requests.get(url+str(i+1))
        soup = BeautifulSoup(response.text,"html.parser")

        chapter_title.append(chapter.get_chapter_title(soup))

        chapter_contents = chapter.get_chapter_contents(soup)
        chapter_contents = string_utils.replace_odd_chars(chapter_contents)

        chapter_list.append(epub.EpubHtml(title=chapter_title[i].text, file_name=chapter_title[i].text + '.xhtml', lang='en'))

        chapter_list[i].content = chapter_contents
        chapter_contents = ""

        book.add_item(chapter_list[i])

    # define CSS style
    style = 'BODY {color: white;}'
    nav_css = epub.EpubItem(uid="style_nav", file_name="style/nav.css", media_type="text/css", content=style)

    # add CSS file
    book.add_item(nav_css)

    for i in range(0, len(chapter_title)):
        book.toc.append((epub.Link(chapter_title[i].text + '.xhtml', chapter_title[i].text, "chapter" + str(i+1) )))

    # basic spine
    book.spine = ['nav']

    for i in range(0, len(chapter_list)):
        book.spine.append(chapter_list[i])

    book.add_item(epub.EpubNcx())
    book.add_item(epub.EpubNav())

    # save in books folder
    epub.write_epub('books/btth.epub', book, {})

generate_ebook()
