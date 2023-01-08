import requests
from bs4 import BeautifulSoup


def get_Spain_politics():  # 바꿔야함
    url = 'https://elpais.com/deportes/'  # 바꿔야함

    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    table = soup.find_all(
        'section', {'class': 'b-d_d b_col-h b_col-o b_st b_st-r-lg'})[0]  # F12로 찾아서 바꿔야함
    l = table.find_all('article')    # F12로 찾아서 바꿔야함

    item = []

    for i in l:
        dic = {}
        dic['country'] = '스페인'  # 바꿔야함
        dic['category'] = '스포츠'  # 바꿔야함
        dic['url'] = i.find('a')['href']    # F12로 찾아서 바꿔야함
        dic['title'] = i.find('a')['href']  # F12로 찾아서 바꿔야함
        item.append(dic)
        if len(item) == 5:
            break

    print(item)
    return item


get_Spain_politics()    # 바꿔야함
