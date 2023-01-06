import requests
from bs4 import BeautifulSoup
from datetime import datetime


def get_china_sports():  # 바꿔야함
    url = 'https://sports.cctv.com/?spm=C96370.PPDB2vhvSivD.E59hodVIdh2C.7'  # 바꿔야함

    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    table = soup.find_all('div', {'class': 'col_w_800'})[0]   # F12로 찾아서 바꿔야함
    l = table.find_all('li')                            # F12로 찾아서 바꿔야함

    item = []

    for i in l:
        dic = {}
        dic['country'] = '중국'  # 바꿔야함
        dic['category'] = '스포츠'  # 바꿔야함
        dic['url'] = i.find('a')['href']    # F12로 찾아서 바꿔야함
        dic['title'] = i.find('a').text     # F12로 찾아서 바꿔야함
        item.append(dic)
        if len(item) == 5:
            break

    print(item)
    return item


get_china_sports()   # 바꿔야함
