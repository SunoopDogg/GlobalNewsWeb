import requests
from bs4 import BeautifulSoup
from datetime import datetime


def get_brazil_politics():  # 바꿔야함
    url = 'https://www.estadao.com.br/politica/eleicoes/'  # 바꿔야함

    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    table = soup.find_all('div', {'class': 'slick-track'})[1]   # F12로 찾아서 바꿔야함
    l = table.find_all('div', {'class': 'slick-slide'})   # F12로 찾아서 바꿔야함

    item = []

    for i in l:
        dic = {}
        dic['country'] = '브라질'  # 바꿔야함
        dic['category'] = '정치'  # 바꿔야함
        dic['url'] = i.find('a')['href']    # F12로 찾아서 바꿔야함
        dic['title'] = i.find('h3').text    # F12로 찾아서 바꿔야함
        item.append(dic)
        if len(item) == 5:
            break

    print(item)
    return item
