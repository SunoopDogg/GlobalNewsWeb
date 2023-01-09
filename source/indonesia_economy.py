import requests
from bs4 import BeautifulSoup


def get_indonesia_economy():  # 바꿔야함
    url = 'https://www.jawapos.com/berita-hari-ini/?date=&category=117893'   # 바꿔야함

    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    table = soup.find_all('div', {'class': 'post-list'})[0]  # F12로 찾아서 바꿔야함
    l = table.find_all('h3', {'class': 'post-list__title'})  # F12로 찾아서 바꿔야함

    item = []

    for i in l:
        dic = {}
        dic['country'] = '인도네시아'   # 바꿔야함
        dic['category'] = '경제'  # 바꿔야함
        dic['url'] = i.find('a')['href']    # F12로 찾아서 바꿔야함
        dic['title'] = i.find('a')['title']  # F12로 찾아서 바꿔야함
        item.append(dic)
        if len(item) == 5:
            break

    print(item)
    return item
