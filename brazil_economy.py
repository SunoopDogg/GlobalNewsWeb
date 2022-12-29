import requests
from bs4 import BeautifulSoup

from DB.insert_item import insertItem
from DB.my_db import getLocalDB

url = 'https://www.estadao.com.br/economia/#google_vignette'   # 동일 바꿔야함

r = requests.get(url)   # 동일

soup = BeautifulSoup(r.text, 'html.parser')  # 동일

table = soup.find_all('ul', {'class': 'bullets --length-4'})[0]
l = table.find_all('li')

item = []   # 동일

for i in l:  # 동일
    dic = {}  # 동일
    dic['country'] = '브라질'   # 동일 바꿔야함
    dic['category'] = '경제'  # 동일 바꿔야함
    dic['url'] = i.find('a')['href']
    dic['title'] = i.find('a')['title']
    item.append(dic)  # 동일
    if len(item) == 5:  # 동일
        break  # 동일

print(item)

# # db에 저장
# print('db에 저장')  # 동일
# db = getLocalDB()  # 동일
# insertItem(db, item)  # 동일
# db.close()  # 동일
