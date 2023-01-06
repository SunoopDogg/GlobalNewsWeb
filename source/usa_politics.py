import requests
from bs4 import BeautifulSoup
from datetime import datetime


def get_usa_politics():  # 바꿔야함
    url = 'https://edition.cnn.com/politics'  # 바꿔야함

    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    table = soup.find_all('div', {'class': 'container__field-wrapper container_lead-plus-headlines__field-wrapper'})[0]   # F12로 찾아서 바꿔야함
    l = table.find_all('div', {'data-unselectable': 'true'})   # F12로 찾아서 바꿔야함

    item = []

    for i in l:
        dic = {}
        dic['country'] = '미국'  # 바꿔야함
        dic['category'] = '정치'  # 바꿔야함
        dic['url'] = i.find('a')['href']    # F12로 찾아서 바꿔야함
        dic['title'] = i.find('a').text     # F12로 찾아서 바꿔야함
        item.append(dic)
        if len(item) == 5:
            break

    print(item)
    return item


get_usa_politics()   # 바꿔야함
