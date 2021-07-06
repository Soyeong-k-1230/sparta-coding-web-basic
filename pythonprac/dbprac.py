from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

# 코딩 시작
# insert, find, update, delete

# insert
# doc = {'name': 'Jane', 'age': 21}
# db.users.insert_one(doc)

# find
# same_ages = list(db.users.find({'age': 21}, {'_id': False}))
same_ages = list(db.users.find({}, {'_id': False}))
for person in same_ages:
    print(person)

print(same_ages)
# find_one
# user = db.users.find_one({'name':'bobby'}, {'_id': False})
# print(user)

# update
db.users.update_one({'name':'bobby'},{'$set':{'age':19}})

# 이름이 모두 bobby인 데이터를 모두 바꿔라, 자주 사용하지는 않는다.
# db.users.update_many({'name':'bobby'},{'$set':{'age':19}})

# delete
db.users.delete_one({'name': 'bobby'})
# delete_many 도 있음

# 저장 - 예시
doc = {'name':'bobby','age':21}
db.users.insert_one(doc)

# 한 개 찾기 - 예시
user = db.users.find_one({'name':'bobby'})

# 여러개 찾기 - 예시 ( _id 값은 제외하고 출력)
same_ages = list(db.users.find({'age':21},{'_id':False}))

# 바꾸기 - 예시
db.users.update_one({'name':'bobby'},{'$set':{'age':19}})

# 지우기 - 예시
db.users.delete_one({'name':'bobby'})

