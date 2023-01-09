import requests
from bs4 import BeautifulSoup


def get_indonesia_sports():  # 바꿔야함
    url = 'https://www.jawapos.com/sports/'   # 바꿔야함

    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    table = soup.find_all(
        'div', {'class': 'post-list post-list--child post-list--noborder'})[0]
    l = table.find_all('h3', {'class': 'post-list__title'})

    item = []

    for i in l:
        dic = {}
        dic['country'] = '인도네시아'   # 바꿔야함
        dic['category'] = '스포츠'  # 바꿔야함
        dic['url'] = i.find('a')['href']
        dic['title'] = i.find('a')['title']
        item.append(dic)
        if len(item) == 5:
            break

    print(item)
    return item
