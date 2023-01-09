import requests
from bs4 import BeautifulSoup
from datetime import datetime


def get_mexico_politics():  # 바꿔야함
    url = 'https://www.nbcnews.com/politics'  # 바꿔야함

    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    table = soup.find_all('div', {'class': 'styles_itemsContainer__saJYW'})[
        0]   # F12로 찾아서 바꿔야함
    l = table.find_all(
        'div', {'class': 'wide-tease-item__wrapper'})   # F12로 찾아서 바꿔야함

    item = []

    for i in l:
        dic = {}
        dic['country'] = '멕시코'  # 바꿔야함
        dic['category'] = '정치'  # 바꿔야함
        dic['url'] = i.find('a')['href']    # F12로 찾아서 바꿔야함
        dic['title'] = i.find(
            'h2', {'class': 'wide-tease-item__headline'}).text     # F12로 찾아서 바꿔야함
        item.append(dic)
        if len(item) == 5:
            break

    print(item)
    return item


if __name__ == '__main__':
    get_mexico_politics()   # 바꿔야함
