import requests
from bs4 import BeautifulSoup


def get_malaysia_economy():  # 바꿔야함
    url = 'https://www.thesundaily.my/business'  # 바꿔야함

    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    table = soup.find_all('div', {'class': '_2477831277_teaser_paged'})[1]  # F12로 찾아서 바꿔야함
    l = table.find_all('div', {'class': 'headline'})    # F12로 찾아서 바꿔야함

    item = []

    for i in l:
        dic = {}
        dic['country'] = '말레이시아'  # 바꿔야함
        dic['category'] = '경제'  # 바꿔야함
        dic['url'] = i.find('a')['href']    # F12로 찾아서 바꿔야함
        dic['title'] = i.find('h2').text  # F12로 찾아서 바꿔야함
        item.append(dic)
        if len(item) == 5:
            break

    print(item)
    return item


get_malaysia_economy()    # 바꿔야함