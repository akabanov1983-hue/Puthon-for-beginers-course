# li = [0, 1, 2, 3, 4, 5]
#
# def func(x):
#     x[-1] = -3
#     return
#
#
# # list - изменяемый, есть проблемы со ссылками (copy, deepcopy)
# func(li)
# print(li)
#
#
# def func(x):
#     print(x, id(x))
#     print(li, id(li))
#     x[-1] = -3
#     print(x, id(x))
#     print(li, id(li))
#     print()
#     return
#
#
# def summa(a, b):
#     return a * b
#     return a - b
#     return a ** b
#     return a / b
#     return a + b
#     return a % b
#
# print(summa(4, 6))

# def swapXandY(x, y):
#     z = x
#     x = y
#     y = z

# 13-04-2026 Исключения и тестирование

# for i in range(5):
#     try:
#         # ZeroDivisionError ValueError
#         # raise ZeroDivisionError
#         # raise ValueError
#         # raise AttributeError
#         cash = int(input("Введите сумму для накопления: "))
#         m = int(input("Срок накопления в месяцах: "))
#         res = cash / m
#         print(f'Тебе нужно откладывать {res} в месяц, чтобы за {m} месяцев накопить {cash}')
#
#     except ZeroDivisionError as e:
#         print("Делить на ноль нельзя")
#         print(e.args)
#     except ValueError as e:
#         print('Введено не целое число')
#         print(e.args)
#     except:
#         print("Возникла ошибка, побробуйте еще раз")

