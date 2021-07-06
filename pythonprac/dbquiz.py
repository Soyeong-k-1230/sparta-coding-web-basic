from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

# 1
rating = db.movies.find_one({'title': '매트릭스'}, {'_id': False})
print(rating['rating'])
# 2
movies = db.movies.find({'rating': rating['rating']}, {'_id': False})
for movie in movies:
    print(movie['title'])
# 3
db.movies.update_one({'title': '매트릭스'}, {'$set': {'rating': '0'}})
