import requests
from bs4 import BeautifulSoup


def get_southarabia_sports():  # 바꿔야함
    url = 'https://www.okaz.com.sa/economy'  # 바꿔야함

    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    table = soup.find_all(
        'div', {'class': 'section-body widget-header'})[1]    # F12로 찾아서 바꿔야함
    l = table.find_all('li', {'class': 'update'})   # F12로 찾아서 바꿔야함

    item = []

    for i in l:
        dic = {}
        dic['country'] = '사우디아라비아'   # 바꿔야함
        dic['category'] = '스포츠'    # 바꿔야함
        dic['url'] = i.find('a')['href']    # F12로 찾아서 바꿔야함
        dic['title'] = i.find('a').text   # F12로 찾아서 바꿔야함
        item.append(dic)
        if len(item) == 5:
            break

    print(item)
    return item
