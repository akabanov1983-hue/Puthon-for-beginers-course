# # rep
#
# def summa(a, b):
#     return a + b
# res = summa(3, 8) # выдаст ошибку, если не задать параметры, или меньшее или большее количество
#
# print(res)
#
# def raznost(a, b):
#     return a - b
#
# print(raznost(8,120))

# message = "Привет! это послание из прошлого, передай его!"
# key = 1000
# print(message)
#
# secured_message = ""
#
# for i in message:
#     secured_message += chr(ord(i)+key)
#
# print(secured_message)
#
# print("Дешивровка....")
# for i in secured_message:
#     print(chr(ord(i)-key), end="")


# def give_me_message(text):
#     message = input(text)
#
#     return message
#
# key = 8

# def shifr(message, k):
#     secured_message = ''
#     for i in message:
#         secured_message += chr(ord(i) + k)
#     return secured_message
#
#
# msg = give_me_message('Введите текст для шифрования')
#
# res_msg = shifr(msg, key)
#
# print(res_msg)
#
# def de_shifr(secured_message, k):
#     print('Дешифровка...')
#     q = ''
#     for i in secured_message:
#         q += chr(ord(i) - k)
#     return q
#
#
#
# de_res_msg = de_shifr(res_msg, key)
#
# print(de_res_msg)
#
#
# def runAPP()
#     user_input = int(input('1 - зашифровать, 2 - дешифровать, 0 - выход'))
#
# def GiveMeTheMessage(text):
#     message = input(text)
#     return message
#
#
# def zashifrovatb(message, k):
#     secured_message = ""
#     for i in message:
#         secured_message += chr(ord(i)+k)
#     return secured_message
#
#
# def deshifrovka(secured_message, k):
#     print("Дешивровка....")
#     q = ""
#     for i in secured_message:
#         q += chr(ord(i)-k)
#     return q
#
#
# def runApp():
#     userInput = int(input("1 - зашифровать, 2 - дешифровать, 0 - выход"))
#     while userInput != 0:
#         key = int(input("Введи ключ для шифра(число целое не отрицательное):"))
#         msg = GiveMeTheMessage("Введи сообщение для послания которе нужно обработать:")
#
#     if userInput == 1:
#         res_msg = zashifrovatb(msg, key)
#         print(res_msg)
#     elif userInput == 2:
#         de_res_msg = deshifrovka(res_msg, key)
#         print(de_res_msg)
#     else:
#         print("Я не понял тебя. повтори ввод заново")
#
#     userInput = int(input("1 - зашифровать, 2 - дешифровать, 0 - выход"))
#
# runApp()

# def registration(name, phone, sername='-',  email='-'):
#     print('Hello', name, phone, sername, email)
#
# registration('ssss', '1123')
# registration('ssss', '1123', 'ppppp')
#
#
# def summa(a=10, b=11):
#     print(a + b)
#
# summa()
#
# summa(b=888)

# summa(12)

# def one():
#     return  1
# res = one()
#
# print(res)
#
# def empty():
#     pass
#
# print(empty())
#
# def mul(a, b):
#     '''
#     Эта функция умножает 2 числа
#     Аргументы
#     а
#     б
#     Возвращает целое число
#
#     '''
#     res = a * b
#     return res
#
# print(help(mul))
#
# print(id(mul))

# def check_age(age):
#     if age >= 18:
#         return True
#     else:
#         return False
#
#
# res = check_age(15)
#
# print(res)

# def check_age(age):
#     return age >= 18

# LEGB
# локальная и глобальная область видимости

# nnn = 99999  # глобальная переменная
#
# def h(n):
#     n = 999 + nnn  # локальная переменная
#     print(n)
#     n = 'ssdfgg'
#     print(n)
#
# print(h(5))

# age = 20
#
# def grow_up(age_1, n):
#     age_1 += n
#     return age_1
#
# print(grow_up(age, 45))

# факториал

# функция факториал(n)

# n = 5  факториал = 1*2*3*4*5

# def my_factorial(n):
#     if n < 0:
#         return None
#     if n <= 1:
#         return 1
#
#     res = 1
#
#     for i in range(2, n + 1):
#         res *= i
#
#     return res
#
#
# def run():
#     li = [-999, 0, 1, 9, 2, 5]
#     res_list = [None, 1, 1, 362880, 2, 120]
#
#     for num, result in zip(li, res_list):
#         if my_factorial(num) == result:
#             print('ok')
#         else:
#             print('faled')
#             print("Ожидалось:", num, result)
#             print("А получилось:", num, my_factorial(num))
#
# run()