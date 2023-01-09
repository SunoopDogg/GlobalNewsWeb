import requests
from bs4 import BeautifulSoup


def get_brazil_sports():  # 바꿔야함
    url = 'https://www.estadao.com.br/esportes/'   # 바꿔야함

    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    table = soup.find_all(
        'div', {'class': 'news-list'})[0]  # F12로 찾아서 바꿔야함
    l = table.find_all(
        'div', {'class': 'noticias-mais-recenter--item'})  # F12로 찾아서 바꿔야함

    item = []

    for i in l:
        dic = {}
        dic['country'] = '브라질'   # 바꿔야함
        dic['category'] = '스포츠'  # 바꿔야함
        dic['url'] = i.find('a')['href']    # F12로 찾아서 바꿔야함
        dic['title'] = i.find('h3', {'class': 'headline'}
                              ).text   # F12로 찾아서 바꿔야함
        item.append(dic)
        if len(item) == 5:
            break

    print(item)
    return item
