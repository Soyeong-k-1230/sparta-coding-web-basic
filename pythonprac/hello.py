# 변수, 자료형, 함수, 조건문, 반복문
first_name = 'Soyeong'
last_name = 'Kim'

print(first_name + last_name)

a_list = ['apple', 'pear', 'pineapple']
print(a_list)

a_list.append('grape')
print(a_list)

a_dict = {'name': 'soyeong', 'age': 27}
print(a_dict['age'])
a_dict['height'] = 168

print(a_dict)

def sum_num(a, b):
    print('hello')
    return a + b

result = sum_num(2, 3)
print(result)

age = 25
if age > 20:
    print('adult')
else:
    print('adolescent')

def is_adult(age):
    if age > 20:
        print('adult')
    else:
        print('adolescent')

is_adult(30)
is_adult(15)

fruits = ['사과','배','배','감','수박','귤','딸기','사과','배','수박']

count = 0
for fruit in fruits:
    print(fruit)
    if fruit == '수박':
        count += 1

print(count)

people = [{'name': 'bob', 'age': 20},
          {'name': 'carry', 'age': 38},
          {'name': 'john', 'age': 7},
          {'name': 'smith', 'age': 17},
          {'name': 'ben', 'age': 27}]

for person in people:
    print(person['name'], person['age'])
    if person['age'] < 20:
        print(person)






