from bs4 import BeautifulSoup
import requests

class Chapter:
    def __init__(self):
        self.id = ""
        self.title = ""
        self.link = ""

response = requests.get("https://www.wuxiaworld.com/novel/battle-through-the-heavens")
soup = BeautifulSoup(response.text,"html.parser")

result = soup.find_all("div",class_="p-15")[0].find_all("li", class_="chapter-item")

def getChaptersList(chapter_soup):
    chapters_list = []
    
    for i, p in enumerate(result):
        chapter = Chapter()

        chapter.id = i
        chapter.link = p.find('a').get('href')
        chapter.title = p.find('span').text

        chapters_list.append(chapter)

    return chapters_list
