import requests
from bs4 import BeautifulSoup
from datetime import datetime


def get_china_politics():  # 바꿔야함
    url = 'https://news.cctv.com/china/?spm=C94212.PZd4MuV7QTb5.En9cOZ8lC46M.2'  # 바꿔야함

    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    table = soup.find_all('ul', {'id': 'newslist'})[0]   # F12로 찾아서 바꿔야함
    l = table.find_all('li')                            # F12로 찾아서 바꿔야함
    print(table)

    item = []

    for i in l:
        dic = {}
        dic['country'] = '중국'  # 바꿔야함
        dic['category'] = '정치'  # 바꿔야함
        dic['url'] = i.find('a')['href']    # F12로 찾아서 바꿔야함
        dic['title'] = i.find('a').text     # F12로 찾아서 바꿔야함
        item.append(dic)
        if len(item) == 5:
            break

    print(item)
    return item


get_china_politics()   # 바꿔야함
