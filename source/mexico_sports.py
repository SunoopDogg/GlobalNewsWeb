import requests
from bs4 import BeautifulSoup
from datetime import datetime


def get_mexico_sports():  # 바꿔야함
    url = 'https://www.nbcsports.com/?cid=eref:nbcnews:text'  # 바꿔야함

    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    table = soup.find_all(
        'div', {'class': 'top-stories__stories-list'})[0]   # F12로 찾아서 바꿔야함
    l = table.find_all('div', {'class': 'list-item'})   # F12로 찾아서 바꿔야함

    item = []

    for i in l:
        dic = {}
        dic['country'] = '멕시코'  # 바꿔야함
        dic['category'] = '스포츠'  # 바꿔야함
        dic['url'] = i.find('a')['href']    # F12로 찾아서 바꿔야함
        dic['title'] = i.find('span').text     # F12로 찾아서 바꿔야함
        item.append(dic)
        if len(item) == 5:
            break

    print(item)
    return item
