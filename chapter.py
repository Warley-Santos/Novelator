from bs4 import BeautifulSoup

def get_chapter_title(soup):
    return soup.findAll('div',{'class':'fr-view'})[0].findAll('p',{'class':''})[0]

def get_chapter_contents(soup):
    chapter_contents = ""
    for p in soup.findAll('div',{'class':'fr-view'})[0].findAll('p',{'class':''}):
        if (p.text.strip() != ""):
            chapter_contents += str(p).strip()+"\r\n"
    return chapter_contents