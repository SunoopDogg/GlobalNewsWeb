from DB.insert_item import insertItem
from DB.my_db import getLocalDB
from source.Australia_economics import get_Australia_economics
from source.Australia_politics import get_Australia_politics
from source.Australia_sport import get_Australia_sports
from source.argentina_economics import get_argentina_economics
from source.argentina_politics import get_argentina_politics
from source.argentina_sports import get_argentina_sports
from source.brazil_economy import get_brazil_economy
from source.brazil_politics import get_brazil_politics
from source.brazil_sports import get_brazil_sports
from source.canada_economics import get_canada_economics
from source.canada_politics import get_canada_politics
from source.canada_sports import get_canada_sports
from source.china_economy import get_china_economics
from source.china_politics import get_china_politics
from source.china_sports import get_china_sports
from source.france_economy import get_france_economics
from source.france_politics import get_france_politics
from source.france_sports import get_france_sports
from source.indonesia_economy import get_indonesia_economy
from source.indonesia_politics import get_indonesia_politics
from source.indonesia_sports import get_indonesia_sports
from source.japan_economics import get_japan_economics
from source.japan_politics import get_japan_politics
from source.japan_sports import get_japan_sports
from source.mexico_economics import get_mexico_economics
from source.mexico_politics import get_mexico_politics
from source.mexico_sports import get_mexico_sports
from source.russia_economics import get_russia_economics
from source.russia_politics import get_russia_politics
from source.russia_sports import get_russia_sports
from source.southarabia_economy import get_southarabia_economy
from source.southarabia_sports import get_southarabia_sports
from source.southkorea_economics import get_southkorea_economics
from source.southkorea_politics import get_southkorea_politics
from source.southkorea_sports import get_southkorea_sports
from source.uk_economics import get_uk_economics
from source.uk_politics import get_uk_politics
from source.uk_sports import get_uk_sports
from source.usa_economy import get_usa_economy
from source.usa_politics import get_usa_politics
from source.usa_sportd import get_usa_sports

item = []

print('start')

print('get argentina politics')
item += get_argentina_politics()  # 아르헨티나 정치
item += get_argentina_economics()  # 아르헨티나 경제
item += get_argentina_sports()  # 아르헨티나 스포츠

print('get australia politics')
item += get_Australia_politics()  # 호주 정치
item += get_Australia_economics()  # 호주 경제
item += get_Australia_sports()  # 호주 스포츠

print('get brazil politics')
item += get_brazil_politics()  # 브라질 정치
item += get_brazil_economy()  # 브라질 경제
item += get_brazil_sports()  # 브라질 스포츠

print('get canada politics')
item += get_canada_politics()  # 캐나다 정치
item += get_canada_economics()  # 캐나다 경제
item += get_canada_sports()  # 캐나다 스포츠

print('get china politics')
item += get_china_politics()  # 중국 정치
item += get_china_economics()  # 중국 경제
item += get_china_sports()  # 중국 스포츠

print('get france politics')
item += get_france_politics()  # 프랑스 정치
item += get_france_economics()  # 프랑스 경제
item += get_france_sports()  # 프랑스 스포츠

print('get germany politics')
item += get_indonesia_politics()  # 인도네시아 정치
item += get_indonesia_economy()  # 인도네시아 경제
item += get_indonesia_sports()  # 인도네시아 스포츠

print('get india politics')
item += get_japan_politics()  # 일본 정치
item += get_japan_economics()  # 일본 경제
item += get_japan_sports()  # 일본 스포츠

print('get indonesia politics')
item += get_mexico_politics()  # 멕시코 정치
item += get_mexico_economics()  # 멕시코 경제
item += get_mexico_sports()  # 멕시코 스포츠

print('get japan politics')
item += get_russia_politics()  # 러시아 정치
item += get_russia_economics()  # 러시아 경제
item += get_russia_sports()  # 러시아 스포츠

print('get maxico politics')
item += get_southarabia_economy()  # 사우디아라비아 경제
item += get_southarabia_sports()  # 사우디아라비아 스포츠

print('get russia politics')
item += get_southkorea_politics()  # 한국 정치
item += get_southkorea_economics()  # 한국 경제
item += get_southkorea_sports()  # 한국 스포츠

print('get south arabia politics')
item += get_uk_politics()  # 영국 정치
item += get_uk_economics()  # 영국 경제
item += get_uk_sports()  # 영국 스포츠

print('get south korea politics')
item += get_usa_politics()  # 미국 정치
item += get_usa_economy()  # 미국 경제
item += get_usa_sports()  # 미국 스포츠

# db에 저장
print('db에 저장')  # 동일
db = getLocalDB()  # 동일
insertItem(db, item)  # 동일
db.close()  # 동일
