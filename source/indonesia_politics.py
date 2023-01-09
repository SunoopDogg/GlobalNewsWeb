import requests
from bs4 import BeautifulSoup


def get_indonesia_politics():   # 바꿔야함
    url = 'https://www.jawapos.com/nasional/politik/'  # 바꿔야함

    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    table = soup.find_all(
        'section', {'class': 'main-section'})[1]  # F12로 찾아서 바꿔야함
    l = table.find_all('div', {'class': 'post-list__item'})  # F12로 찾아서 바꿔야함

    item = []

    for i in l:
        dic = {}
        dic['country'] = '인도네시아'  # 바꿔야함
        dic['category'] = '정치'  # 바꿔야함
        dic['url'] = i.find('a')['href']    # F12로 찾아서 바꿔야함
        dic['title'] = i.find('a')['title']  # F12로 찾아서 바꿔야함
        item.append(dic)
        if len(item) == 5:
            break

    print(item)
    return item
