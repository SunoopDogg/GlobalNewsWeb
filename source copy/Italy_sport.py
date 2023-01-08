import requests
from bs4 import BeautifulSoup


def get_Italy_sport():  # 바꿔야함
    url = 'https://www.corriere.it/sport/'  # 바꿔야함

    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    table = soup.find_all(
        'div', {'column is-8 is-pd-t-0'})[0]  # F12로 찾아서 바꿔야함
    l = table.find_all('div')    # F12로 찾아서 바꿔야함

    item = []

    for i in l:
        dic = {}
        dic['country'] = '이탈리아'  # 바꿔야함
        dic['category'] = '스포츠'  # 바꿔야함
        dic['url'] = i.find('a')['href']   # F12로 찾아서 바꿔야함
        #dic['title'] = i.find('a', {'has-text-black'}).text #!!!!!!!제목 파트 못 찾겠음!!!!!!!
        item.append(dic)
        if len(item) == 5:
            break

    print(item)
    return item


get_Italy_sport()    # 바꿔야함
