import requests
from bs4 import BeautifulSoup
from datetime import datetime


def get_russia_sports():  # 바꿔야함
    url = 'https://spb.mk.ru/sport/'  # 바꿔야함

    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    table = soup.find_all('ul', {'class': 'article-listing__day-list'})[0]   # F12로 찾아서 바꿔야함
    l = table.find_all('li', {'class': 'article-listing__item'})   # F12로 찾아서 바꿔야함

    item = []

    for i in l:
        dic = {}
        dic['country'] = '러시아'  # 바꿔야함
        dic['category'] = '스포츠'  # 바꿔야함
        dic['url'] = i.find('a')['href']    # F12로 찾아서 바꿔야함
        dic['title'] = i.find('h3').text     # F12로 찾아서 바꿔야함
        item.append(dic)
        if len(item) == 5:
            break

    print(item)
    return item


get_russia_sports()   # 바꿔야함
