import requests
from bs4 import BeautifulSoup


def get_uk_sports():  # 바꿔야함 // 진행중
    url = 'https://www.theguardian.com/uk/sport'  # 바꿔야함

    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    table = soup.find_all('div', {'class': 'fc-slice-wrapper'})[2]    # F12로 찾아서 바꿔야함
    l = table.find_all('li', {'class': 'fc-slice__item'})   # F12로 찾아서 바꿔야함

    item = []

    for i in l:
        dic = {}
        dic['country'] = '영국'   # 바꿔야함
        dic['category'] = '스포츠'    # 바꿔야함
        dic['url'] = i.find('a')['href']    # F12로 찾아서 바꿔야함
        dic['title'] = i.find('a').text   # F12로 찾아서 바꿔야함
        item.append(dic)
        if len(item) == 5:
            break

    print(item)
    return item


get_uk_sports()   # 바꿔야함
