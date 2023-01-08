import requests
from bs4 import BeautifulSoup


def get_japan_economics():  # 바꿔야함 // 진행중
    url = 'https://www.yomiuri.co.jp/economy/'  # 바꿔야함

    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    table = soup.find_all(
        'ul', {'class': 'p-category-organization-sec-list'})[0]    # F12로 찾아서 바꿔야함
    l = table.find_all('li', {'class': 'p-list-item'})   # F12로 찾아서 바꿔야함

    item = []

    for i in l:
        dic = {}
        dic['country'] = '일본'   # 바꿔야함
        dic['category'] = '경제'    # 바꿔야함
        dic['url'] = i.find('a')['href']    # F12로 찾아서 바꿔야함
        dic['title'] = i.find(
            'h3', {'class': 'c-list-title'}).find('a').text  # F12로 찾아서 바꿔야함
        item.append(dic)
        if len(item) == 5:
            break

    print(item)
    return item


get_japan_economics()   # 바꿔야함
