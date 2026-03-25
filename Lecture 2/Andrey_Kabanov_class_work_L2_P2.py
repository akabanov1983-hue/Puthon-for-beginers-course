# # # сравнения
# # # == равно
# # # != не равно
# # # > больше
# # # < меньше
# # # >= больше, либо равно
# # # <= меньше, либо равно
# #
# #
# # age = 19
# #
# # print(age > 18)
# #
# # print(age == 18)
# #
# # print(age < 18)
# #
# # print(18 > 18)
# #
# # print(18 == 18)
#
# #  Результат сравнения всегда возвращает булево число True/False.
#
# # 25-03-2026
#
# # print(1234)
# #
# # print(1, 2, 3, 4, 5, sep=')')
# #
# # age = 9999
# #
# # print(age)
# #
# # type(age)
# #
# # nubmer = input('Введите число')
# #
# # nubmer = int(nubmer)
# #
# # isinstance(nubmer, int)
# #
# # print(nubmer/2)
#
# # Условия.
#
# # Условие начинается с if
#
# # if condition:
# #     action_true
# # else:
# #   action_false
#
# # password = '1234*'
# #
# # if password == '12345':
# #     print('OK')
# # else:
# #     print('Неверный пароль')
#
#
# # age = -5
# #
# # if age < 7:
# #     print('Детский сад')
# # elif age <= 14:
# #     print('подросток')
# # else:
# #     print('Взрослый')
#
#
# # age = 17
# # if age < 7:
# #     print('Детский сад')
# # elif age <= 14:
# #     print('подросток')
# # elif age <= 18:
# #     print('Старшая школа')
# # else:
# #     print('Взрослый')
#
#
# # Однострочники
#
# # key = '777'
# #
# # if key == '777':
# #     print('1')
# # else:
# #     print(2)
# #
# # chek = True if key == '777' else False
# #
# # if chek:
# #     print('1')
# # else:
# #     print(2)
#
# # Поиск наибольшего числа из двух
#
# # number1, number2 = int(input('num1: ')), int(input('num2: '))
# # result = 0
# #
# # if number1 > number2:
# #     result = number1
# # else:
# #     result = number2
# # print(result)
#
# # match/case
#
# # age = 14
# # match age:
# #     case age 7:
# #         print('Детский сад')
# #     case age 14:
# #         print('подросток')
# #     case age 18:
# #         print('Старшая школа')
# #     case _:
# #         print('Взрослый')
#
# # ЦИКЛЫ
#
# # while цикл
#
# # text = 'Привет'
# #
# # counter = 1
# #
# # while counter <= 5:  # Для любого цикла необходимо завершение
# #     print(counter, text)
# #     counter += 1
#
# # result = 0
# #
# # number = int(input('Введи число или 0 для выхода из цикла: '))
# #
# # while number != 0:
# #     result += number
# #     number = int(input('Введи число или 0 для выхода из цикла: '))
#
# # print(help(range))
#
# # for number in range(1, 10):
# #     print(number, end=' ')
# # print()
# #
# # for number in range(10):
# #     print(number, end=' ')
# # print()
# #
# # for number in range(1, 10, 2):
# #     print(number, end=' ')
# # print()
#
# # for i in range(1,11):
# #     print(i**i)
#
# import time
#
# # print(help(time))
#
# # for i in range(5):
# #     print("Не спи!!!", i)
# #     time.sleep(1)
#
#
# # break / continue - используются только внутри цикла
#
# # break - прекращение или выход из цикла
# # for i in range(5):
# #     if i == 4:
# #         break
# #     print("Не спи!!!", i)
#
# # continue - пропускает значение
# # for i in range(5):
# #     if i == 3:
# #         continue
# #     print("Не спи!!!", i)
#
# # hp = 100
# # time_limit = 60
# #
# # while time_limit >= 0:
# #
# #     if hp <=0:
# #         break
# #
# #     print(time_limit)
# #     print(hp)
# #
# #     if time_limit %2 == 0:
# #         hp -= 15
# #     if time_limit % 2 != 0:
# #         time_limit -= 1
#
#
# # in/not in
#
# # word = 'слово'
# # print('а' in word)
# #
# # file = ''' ddddddddddddddddddddddddddddddd
# # dddddddddddddddddddddddddddddd
# # dddddddddddddddddddddddddddd
# # dddddddddddddd123'''
# #
# # if '123' in file:
# #     print('Да')
# # else:
# #     print('Нет')
#
# # name = 'aaaaaaaa'
# #
# # print(name.upper())
#
#
# # name = 'aaabbsssdfff'
# #
# # for ch in name:
# #     if ch == 'b':
# #         continue
# #     print(ch.upper(),ch*7)
#
#
# # not and or
#
# name = 'X'
#
# phone = '123'
#
# age = 19
#
# if name == 'X' and phone == '123' and age == 18:
#     print('Все три условия совпали')
#
# if name == 'X' or phone == '123' or age == 18:
#     print('Что-то совпало')