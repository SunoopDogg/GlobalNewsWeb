import requests
from bs4 import BeautifulSoup


def get_Australia_politics():
    url = 'https://www.smh.com.au/politics'  # 바꿔야함

    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    table = soup.find_all(
        'div', {'class': 'Ymd-f'})[0]  # F12로 찾아서 바꿔야함
    l = table.find_all('h3', {'class': '_2XVos'})  # F12로 찾아서 바꿔야함

    item = []

    for i in l:
        dic = {}
        dic['country'] = '호주'  # 바꿔야함
        dic['category'] = '정치'  # 바꿔야함
        dic['url'] = i.find('a')['href']    # F12로 찾아서 바꿔야함
        dic['title'] = i.find('a')['href']  # F12로 찾아서 바꿔야함
        item.append(dic)
        if len(item) == 5:
            break
    
    print(item)
    return item
