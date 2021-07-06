import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200303',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

# 코딩 시작
title = soup.select_one('#old_content > table > tbody > tr:nth-child(2) > td.title > div > a')
print(title)
print(title.text)
print(title['href'])

#old_content > table > tbody > tr:nth-child(2)
#old_content > table > tbody > tr

trs = soup.select('#old_content > table > tbody > tr')

#old_content > table > tbody > tr:nth-child(2) > td.title > div > a
#old_content > table > tbody > tr:nth-child(2) > td:nth-child(1) > img
#old_content > table > tbody > tr:nth-child(2) > td.point
for tr in trs:
    a_tag = tr.select_one('td.title > div > a')
    rating_tag = tr.select_one('tr > td.point')
    rank_tag = tr.select_one('tr > td > img')

    if a_tag is not None and rating_tag is not None:
        title = a_tag.text
        rating = rating_tag.text
        rank = rank_tag['alt']
        print(rank, title, rating)
        doc = {
            'rank': rank,
            'title': title,
            'rating': rating
        }
        db.movies.insert_one(doc)




