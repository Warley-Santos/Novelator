from ebooklib import epub

def generate_sumary(chapter_title, book):
    for i in range(0, len(chapter_title)):
        book.toc.append((epub.Link(chapter_title[i].text + '.xhtml', chapter_title[i].text, "chapter" + str(i+1) )))
    return book

def append_chapters(book_chapters, book):
    for i in range(0, len(book_chapters)):
        book.spine.append(book_chapters[i])
    return book

def add_nav_ncx(book):
    book.add_item(epub.EpubNcx())
    book.add_item(epub.EpubNav())
    return book

def add_spine(book):
    # basic spine
    book.spine = ['nav']
    return book

def add_css(book):
    # define CSS style
    style = 'BODY {color: white;}'
    nav_css = epub.EpubItem(uid="style_nav", file_name="style/nav.css", media_type="text/css", content=style)

    # add CSS file
    book.add_item(nav_css)
    return book 