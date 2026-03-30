# # Home work 2.5

# # Необходимо найти наибольшее из четырех целых чисел.
#
# # Запрос 4 чисел.
# num_1 = int(input('Введите первое целое число: '))
# num_2 = int(input('Введите второе целое число: '))
# num_3 = int(input('Введите третье целое число: '))
# num_4 = int(input('Введите четвертое целое число: '))
#
# # Сравнение чисел друг с другом.
# maximum = num_1
# if num_2 > maximum:
#     maximum = num_2
# if num_3 > maximum:
#     maximum = num_3
# if num_4 > maximum:
#     maximum = num_4
#
# print(f'Наибольшим из чисел {num_1}, {num_2}, {num_3}, {num_4} является число {maximum}')


# # Home work 2.5 (lab)
# Пожиратель гласных букв.

# Ввод строки и перевод в верхний регистр.
# user_word = input('Введите строку символов: ').upper()
#
# # Перебор символов строки в цикле и пропуск символов из списка.
# for ch in user_word:
#     if ch in 'AEIOU':
#         continue
#     print(ch)


# # Home work 2.6
# print('Это программа-калькулятор.'
#       'Она производит математические операции над двумя числами.')
#
# operation = input('Введите "+", "-", "*", "/" '
#                   'или "exit" для выхода из программы: ')
#
# while operation != 'exit':
#
#     num_1 = float(input('Введите первое число: '))
#     num_2 = float(input('Введите второе число: '))
#
#     if operation == '+':
#         print(f'{num_1} + {num_2} = {num_1 + num_2}')
#     elif operation == '-':
#         print(f'{num_1} - {num_2} = {num_1 - num_2}')
#     elif operation == '*':
#         print(f'{num_1} * {num_2} = {num_1 * num_2}')
#     elif operation == '/':
#         if num_2 == 0:
#             print('На ноль делить нельзя. Введите число, отличное от нуля')
#         else:
#             print(f'{num_1} / {num_2} = {num_1 / num_2}')
#
#     operation = input('Введите "+", "-", "*", "/" '
#                       'или "exit" для выхода из программы: ')
