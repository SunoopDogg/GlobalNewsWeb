import requests
from bs4 import BeautifulSoup


def get_Italy_economics():  # 바꿔야함
    url = 'https://www.corriere.it/economia/finanza/'  # 바꿔야함

    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    table = soup.find_all(
        'div', {'column is-8'})[0]  # F12로 찾아서 바꿔야함
    l = table.find_all('article')    # F12로 찾아서 바꿔야함

    item = []

    for i in l:
        dic = {}
        dic['country'] = '이탈리아'  # 바꿔야함
        dic['category'] = '경제'  # 바꿔야함
        dic['url'] = i.find('a')['href']    # F12로 찾아서 바꿔야함
        #dic['title'] = i.find('a')['title'] #!!!!!!!제목 파트 못 찾겠음!!!!!!!
        item.append(dic)
        if len(item) == 5:
            break

    print(item)
    return item


get_Italy_economics()    # 바꿔야함