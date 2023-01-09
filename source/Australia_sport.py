import requests
from bs4 import BeautifulSoup


def get_Australia_sports():
    url = 'https://www.smh.com.au/sport'  # 바꿔야함

    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    table = soup.find_all(
        'div', {'class': 'Ymd-f'})[0]  # F12로 찾아서 바꿔야함
    l = table.find_all('div', {'class': '_1YzQk'})  # F12로 찾아서 바꿔야함

    item = []

    for i in l:
        dic = {}
        dic['country'] = '호주'  # 바꿔야함
        dic['category'] = '스포츠'  # 바꿔야함
        dic['url'] = i.find('h3').find('a')['href']    # F12로 찾아서 바꿔야함
        dic['title'] = i.find('h3').find('a').text  # F12로 찾아서 바꿔야함
        item.append(dic)
        if len(item) == 5:
            break

    print(item)
    return item
