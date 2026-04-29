students_grades = {}


def avg(score):
    """Функция вычисления среднего балла студента.
     :argument score - tuple - набор оценок
     :returns flat - средний балл, 2 знака после запятой
    """
    return round((sum(score)) / len(score), 2)


def new_student(student_name):
    """Функция добавляет студента в список студентов по его имени
    :argument student_name - str - имя студента, не менее 2-х символов
    :returns
    True - если студент добавлен успешно
    False - если имя меньше 2-х символов.
    """
    if len(student_name) < 2:
        return False

    student_name = student_name.title()

    if student_name in students_grades:
        print(f'Студент с имеменем {student_name} уже существует')
    else:
        students_grades.update({student_name: ()})
        print(f'Студент {student_name} успешно добавлен')


def del_student(student_name):
    """Функция удаляет студента из списка студентов по его имени"""

    if len(student_name) < 2:
        return False

    student_name = student_name.title()

    if student_name in students_grades:
        students_grades.pop(student_name)
        print(f'Студент с имеменем {student_name} удален')
    else:
        print(f'Студент {student_name} отсутсвует в списке')


def show_students_list():
    """Функция выводит отсортированный список студентов"""
    for student in sorted(students_grades.keys()):
        print(student)



def new_grade(student_name, grade):
    """Функция для добавления новой оценки студенту
    :argument student_name - str - имя студента, не менее 2-х символов
    :argument grade - int - оценка
    :returns
    True - если оценка добавлена успешно
    False - если имя меньше 2-х символов.
    """

    if len(student_name) < 2:
        return False

    student_name = student_name.title()


    if student_name in students_grades:
        students_grades.update(
            {student_name: students_grades.get(student_name) + (grade,)})

    else:
        students_grades.update({student_name: (grade,)})

    return True

def show_grades():
    print('Show grades')
    for key, value in students_grades.items():
        print('name', key)
        print('grade', value)


def show_avg():
    print('Show avg')
    for key, value in students_grades.items():
        print('name', key)
        print('avg', avg(value))



def main():
   msg = """
    Эта программа для вычисления средней оценки студентов
    Введите номер операции:
    
    1 - ввести новую оценку для студента
    2 - показать среднюю оценку
    3 - показать оценки
    4 - добавить нового студента в список
    5 - удалить студента и его оценки
    6 - вывести список всех студентов
    quit - выйти из программы
    """
   operation = input(msg)
   while operation != 'quit':
        match operation:
            case '1':
                name = input("Введите имя студента: ")
                grade = int(input("Введите оценку: "))
                new_grade(name, grade)
            case '2':
                show_avg()
            case '3':
                show_grades()
            case '4':
                name = input("Введите имя студента: ")
                new_student(name)
            case '5':
                name = input("Введите имя студента: ")
                del_student(name)
            case '6':
                show_students_list()
            case _:
                print("Вы ввели неизвестную команду")

        operation = input(msg)

main()
