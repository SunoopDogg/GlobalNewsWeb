from DB.insert_item import insertItem
from DB.my_db import getLocalDB

from source.brazil_economy import get_brazil_economy
from source.brazil_politics import get_brazil_politics

item = get_brazil_politics()  # 브라질 정치
item += get_brazil_economy()  # 브라질 경제

# db에 저장
print('db에 저장')  # 동일
db = getLocalDB()  # 동일
insertItem(db, item)  # 동일
db.close()  # 동일
