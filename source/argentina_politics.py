import requests
from bs4 import BeautifulSoup
from datetime import datetime


def get_argentina_politics():  # 바꿔야함
    url = 'https://www.laprensani.com/politica'  # 바꿔야함

    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    table = soup.find_all(
        'div', {'class': 'content-area'})[0]   # F12로 찾아서 바꿔야함
    l = table.find_all('div', {'class': 'col-12'})   # F12로 찾아서 바꿔야함

    item = []

    for i in l:
        dic = {}
        dic['country'] = '아르헨티나'  # 바꿔야함
        dic['category'] = '정치'  # 바꿔야함
        dic['url'] = i.find('a')['href']    # F12로 찾아서 바꿔야함
        dic['title'] = i.find('h3').text     # F12로 찾아서 바꿔야함
        item.append(dic)
        if len(item) == 5:
            break

    print(item)
    return item
