# int = 1

# print(int)

# # help(input)

# # user_name = input("Введите ваше имя ")

# # print(user_name)

# #print(user_name**2)

# # type casting - приведение одного типа к другому

# a = 'hello'

# b = 100

# c = 3.14

# d = True

# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))


# age = input("Введите возраст ")
# age_int = int(age)
# print(age_int / 2)

# print(isinstance(age_int, int))

# математические операции

# print(2**3**2)

# Строковые операции
# конкатенация - склеить строки
# репликация - умножение строки несколько раз

name = "AAAaa"
age = "14"
phone = '+3755555555'
separator = ' | '
user_data = name + separator + age + separator + phone
print(user_data)

# репликация
print('cat '*99)

name = 'AAAA'
age = '123'
phone = '+37522222'
sep = ' | '

print(f'Имя {name}{sep}{age}{sep}{phone}')

# ключевые слова
import keyword
print(keyword.kwlist)

a, b = int(input("a = ")), int(input("b = "))

print(f'{a} + {b} = {a+b}')
print(f'{a} - {b} = {a-b}')
print(f'{a} * {b} = {a*b}')

import this
