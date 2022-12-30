import requests
from bs4 import BeautifulSoup


def get_brazil_economy():
    url = 'https://www.estadao.com.br/economia/#google_vignette'  # 바꿔야함

    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    table = soup.find_all(
        'ul', {'class': 'bullets --length-4'})[0]  # F12로 찾아서 바꿔야함
    l = table.find_all('li')    # F12로 찾아서 바꿔야함

    item = []

    for i in l:
        dic = {}
        dic['country'] = '브라질'  # 바꿔야함
        dic['category'] = '경제'  # 바꿔야함
        dic['url'] = i.find('a')['href']    # F12로 찾아서 바꿔야함
        dic['title'] = i.find('a')['title']  # F12로 찾아서 바꿔야함
        item.append(dic)
        if len(item) == 5:
            break

    print(item)
    return item
