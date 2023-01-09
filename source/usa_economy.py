import requests
from bs4 import BeautifulSoup
from datetime import datetime


def get_usa_economy():  # 바꿔야함
    url = 'https://www.washingtonpost.com/business/technology/?itid=hp_top_nav_tech'  # 바꿔야함

    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    table = soup.find_all('article', {'class': 'b-l'})[0]   # F12로 찾아서 바꿔야함
    l = table.find_all('div', {'class': 'pb-md'})   # F12로 찾아서 바꿔야함

    item = []

    for i in l:
        dic = {}
        dic['country'] = '미국'  # 바꿔야함
        dic['category'] = '경제'  # 바꿔야함
        dic['url'] = i.find('a')['href']    # F12로 찾아서 바꿔야함
        dic['title'] = i.find('h3').text     # F12로 찾아서 바꿔야함
        item.append(dic)
        if len(item) == 5:
            break

    print(item)
    return item
