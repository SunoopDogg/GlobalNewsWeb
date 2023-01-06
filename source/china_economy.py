import requests
from bs4 import BeautifulSoup
from datetime import datetime


def get_china_economy():  # 바꿔야함
    url = 'https://finance.cctv.com/index.shtml?spm=C94433.Pt3TM2eA7qqo.E2XVQsMhlk44.6'  # 바꿔야함

    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    table = soup.find_all('div', {'class': 'con'})[0]   # F12로 찾아서 바꿔야함
    l = table.find_all('li')                            # F12로 찾아서 바꿔야함
    print(table)

    item = []

    for i in l:
        dic = {}
        dic['country'] = '중국'  # 바꿔야함
        dic['category'] = '경제'  # 바꿔야함
        dic['url'] = i.find('a')['href']    # F12로 찾아서 바꿔야함
        dic['title'] = i.find('a').text     # F12로 찾아서 바꿔야함
        item.append(dic)
        if len(item) == 5:
            break

    print(item)
    return item


get_china_economy()   # 바꿔야함
