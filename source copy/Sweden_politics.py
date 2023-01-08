import requests
from bs4 import BeautifulSoup


def get_Sweden_politics():  # 바꿔야함
    url = 'https://www.dn.se/sverige/'  # 바꿔야함

    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    table = soup.find_all(
        'section', {'class': 'section__column-main'})[0]  # F12로 찾아서 바꿔야함
    l = table.find_all('a')    # F12로 찾아서 바꿔야함

    item = []

    for i in l:
        dic = {}
        dic['country'] = '스웨덴'  # 바꿔야함
        dic['category'] = '정치'  # 바꿔야함
        dic['url'] = i.find('a')['href']    # F12로 찾아서 바꿔야함
        dic['title'] = i.find('h1')['class']  # F12로 찾아서 바꿔야함
        item.append(dic)
        if len(item) == 5:
            break

    print(item)
    return item


get_Sweden_politics()    # 바꿔야함
