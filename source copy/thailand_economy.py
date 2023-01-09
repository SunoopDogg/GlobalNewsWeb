import requests
from bs4 import BeautifulSoup
from datetime import datetime


def get_thailand_economy():  # 바꿔야함
    url = 'https://www.khaosodenglish.com/category/news/business/'  # 바꿔야함

    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    table = soup.find_all('div', {'class': 'td-pb-span8'})[0]   # F12로 찾아서 바꿔야함
    l = table.find_all('div', {'class': 'td_module_10'})   # F12로 찾아서 바꿔야함

    item = []

    for i in l:
        dic = {}
        dic['country'] = '태국'  # 바꿔야함
        dic['category'] = '경제' # 바꿔야함
        dic['url'] = i.find('a')['href']    # F12로 찾아서 바꿔야함
        dic['title'] = i.find('a').text     # F12로 찾아서 바꿔야함
        item.append(dic)
        if len(item) == 5:
            break

    print(item)
    return item


get_thailand_economy()   # 바꿔야함
