import requests
from bs4 import BeautifulSoup


def get_uk_sports():  # 바꿔야함 // 진행중
    url = 'https://www.thedailyscrum.ca/category/sports/'  # 바꿔야함

    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    table = soup.find_all('div', {'class': 'archive-content-wrapper'})[0]    # F12로 찾아서 바꿔야함
    l = table.find_all('article', {'class': 'post'})   # F12로 찾아서 바꿔야함

    item = []

    for i in l:
        dic = {}
        dic['country'] = '캐나다'   # 바꿔야함
        dic['category'] = '스포츠'    # 바꿔야함
        dic['url'] = i.find('a')['href']    # F12로 찾아서 바꿔야함
        dic['title'] = i.find('h2').text   # F12로 찾아서 바꿔야함
        item.append(dic)
        if len(item) == 5:
            break

    print(item)
    return item


get_uk_sports()   # 바꿔야함
