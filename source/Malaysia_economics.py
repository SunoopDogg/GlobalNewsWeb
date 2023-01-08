import requests
from bs4 import BeautifulSoup


def get_Malaysia_economics():  # 바꿔야함
    url = 'https://www.thesundaily.my/business'  # 바꿔야함

    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    table = soup.find_all(
        'div', {'class': 'paged noticias carrusel-list'})[0]  # F12로 찾아서 바꿔야함
    l = table.find_all('div')
    item = []

    for i in l:
        dic = {}
        dic['country'] = '말레이시아'  # 바꿔야함
        dic['category'] = '경제'  # 바꿔야함
        dic['url'] = i.find('a')['href']    # F12로 찾아서 바꿔야함
        dic['title'] = i.find('h2')  # F12로 찾아서 바꿔야함
        item.append(dic)
        if len(item) == 5:
            break

    print(item)
    return item


get_Malaysia_economics()    # 바꿔야함
