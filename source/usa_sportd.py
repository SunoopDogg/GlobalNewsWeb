import requests
from bs4 import BeautifulSoup
from datetime import datetime


def get_usa_sports():  # 바꿔야함
    url = 'https://www.washingtonpost.com/sports/'  # 바꿔야함

    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    table = soup.find_all(
        'div', {'class': 'table-in-grid'})[4]   # F12로 찾아서 바꿔야함
    l = table.find_all('div', {'class': 'card'})   # F12로 찾아서 바꿔야함

    item = []

    for i in l:
        dic = {}
        dic['country'] = '미국'  # 바꿔야함
        dic['category'] = '스포츠'  # 바꿔야함
        dic['url'] = i.find('a')['href']    # F12로 찾아서 바꿔야함
        dic['title'] = i.find('span').text     # F12로 찾아서 바꿔야함
        item.append(dic)
        if len(item) == 5:
            break

    print(item)
    return item
