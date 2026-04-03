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

summa(12)