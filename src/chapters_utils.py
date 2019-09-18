from bs4 import BeautifulSoup
from chapter import Chapter

import requests

def get_chapter_title(soup):
    return soup.findAll('div',{'class':'caption clearfix'})[0].findAll('h4',{'class':''})[0]
    
def get_chapter_contents(soup):
    chapter_contents = ""
    for p in soup.findAll('div',{'class':'fr-view'})[0].findAll('p',{'class':''}):
        if (p.text.strip() != ""):
            chapter_contents += str(p).strip()+"\r\n"
    return chapter_contents

def get_chapters_list(novel_link):
    chapters_list = []
    
    chapter_soup = get_chapter_list_html(novel_link)

    for i, p in enumerate(chapter_soup):
        chapter = Chapter()

        chapter.id = i
        chapter.link = p.find('a').get('href')
        chapter.title = p.find('span').text

        chapters_list.append(chapter)

    return chapters_list

def get_chapter_list_html(novel_link):
    response = requests.get(novel_link)
    
    soup = BeautifulSoup(response.text,"html.parser")

    result = soup.find_all("div",class_="p-15")[0].find_all("li", class_="chapter-item")

    return result