import requests
from bs4 import BeautifulSoup


def get_Poland_politics():  # 바꿔야함
    url = 'https://www.fakt.pl/polityka'  # 바꿔야함

    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    table = soup.find_all(
        'div', {'data-section': 'main'})[1]  # F12로 찾아서 바꿔야함
    l = table.find_all('div')    # F12로 찾아서 바꿔야함

    item = []

    for i in l:
        dic = {}
        dic['country'] = '나라'  # 바꿔야함
        dic['category'] = '카테고리'  # 바꿔야함
        dic['url'] = i.find('a')['href']    # F12로 찾아서 바꿔야함
        #dic['title'] = i.find('h2')['class']
        dic['title'] = i.find('h2', {'class': 'list-item-title'})  # F12로 찾아서 바꿔야함
        item.append(dic)
        if len(item) == 5:
            break

    print(item)
    return item


get_Poland_politics()    # 바꿔야함

