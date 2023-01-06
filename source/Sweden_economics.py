import requests
from bs4 import BeautifulSoup


def get_Sweden_economics():
    url = 'https://www.dn.se/ekonomi/'  # 바꿔야함

    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    table = soup.find_all(
        'div', {'class': 'news-list__container'})[0]  # F12로 찾아서 바꿔야함
    l = table.find_all('div', {'class': 'news-list__container'})  # F12로 찾아서 바꿔야함

    item = []
 
    for i in l:
        dic = {}
        dic['country'] = '호주'  # 바꿔야함
        dic['category'] = '경제'  # 바꿔야함
        dic['url'] = i.find('h3').find('a')['href']    # F12로 찾아서 바꿔야함
        dic['title'] = i.find('h3').find('a').text  # F12로 찾아서 바꿔야함
        item.append(dic)
        if len(item) == 5:
            break
    
    print(item)
    return item

print(get_Sweden_economics())