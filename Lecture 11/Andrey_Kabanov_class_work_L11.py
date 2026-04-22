# # 22-02-2026
#
# class User:
#     counter = 0
#     def __init__(self, name):
#         self.user_name = name
#         User.counter += 1
#
#
#     # альтернативный конструктор
#     @classmethod
#     def alt_init_inc_email_age(cls, name, email, age):
#         _user = cls(name)
#         _user.email = email
#         _user.age = age
#         return _user
#
#
#     def get_name(self):
#         return self.user_name
#
#     def __str__(self):
#         return self.user_name
#
#     def __repr__(self):
#         return f"repr User: name: {self.user_name}"
#
#     @classmethod
#     def double_counter(cls):
#         cls.counter *= 2
#
#     @classmethod
#     def get_counter(cls):
#         return cls.counter
#
#     @staticmethod
#     def pow_two(n):
#         return n ** 2
#
# dima = User("Dima")
#
# vasya = User("Vasya")
#
# print(dima.get_name())
#
# print(dima.pow_two(22))
#
# print(User.pow_two(22))
#
# dima.get_name()
#
# print(User.counter)
#
# new_dima = User.alt_init_inc_email_age('New_dima', 'ssdsssd', 22)
#
# print(new_dima.email)


# # Абстрактный класс
#
# # Задача:
# # делать экспорт из нашего сервиса в форматы:
# # csv, pdf, json
#
# from abc import ABC, abstractmethod
#
# class Task_Export_Data(ABC):
#
#     @abstractmethod
#     def prepare(self):
#         pass
#
#     @abstractmethod
#     def check(self):
#         pass
#
#     @abstractmethod
#     def export(self):
#         pass
#
# class json_data(Task_Export_Data):
#     def __init__(self, data):
#         self.__data = data
#     def check(self):
#         print("чтото проверяю json")
#     def prepare(self):
#         print("чтото подготавливаю json")
#     def export(self):
#         print("чтото экспортирую json")
#         print(self.__data)
#
#
# class pdf_data(Task_Export_Data):
#     def __init__(self, data):
#         self.__data = data
#     def check(self):
#         print("чтото проверяю pdf")
#     def prepare(self):
#         print("чтото подготавливаю pdf ")
#     def export(self):
#         print("чтото экспортирую pdf")
#         print(self.__data)
#
#
# class csv_data(Task_Export_Data):
#     def __init__(self, data):
#         self.__data = data
#     def check(self):
#         print("чтото проверяю csv")
#     def prepare(self):
#         print("чтото подготавливаю csv")
#     def export(self):
#         print("чтото экспортирую csv")
#         print(self.__data)
#
#
# li = [csv_data("a,b,c,d,e"), pdf_data("sdfsdf sdfsdfsd sdfsdfs s dfsdfs"), json_data('{name:"stas", age: 44}')]
#
# for inst in li:
#     inst.prepare()
#     inst.check()
#     inst.export()

# # MRO
#
# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __repr__(self):
#         return f"repr: name:{self.name} |age:{self.age}"
#
#     def speak(self, sound):
#         return f"{self.name} says {sound}"
#
# print(Dog.mro())
#
# class Bulldog(Dog):
#     def walk(self, steps):
#         return f"{self.name} ходит {steps} шагов"
#
#     def speak(self, sound):
#         par_speak = super().speak(sound)
#         par_speak = par_speak.upper()
#         return "Bulldog speak\n" + par_speak
#
# print(Bulldog.mro())

# # Custom Exeptions
#
# try:
#     print(1+1)
# except:
#     print(1)
# else:
#     print('Ошибок не было')
# finally:
#     print('Работает всегда')

# class EmptyStorageError(Exception):
#     pass
#
#
# class Storage:
#     def __init__(self):
#         self.__items = []
#
#     def priemka(self, value):
#         self.__items.append(value)
#         print("Приемка товара на склад:", value)
#
#     def otgruzka(self):
#         if len(self.__items) == 0:
#             raise EmptyStorageError("На складе нет товара!!!")
#
#     def get_items(self):
#         return self.__items
#

# class App:
#     def __init__(self, storage):
#         self.storage = storage
#
#     def run(self):
#         oper = input("Oper: 1 - приемка, 2 - отгрузка, 3 - вывод всех товаров, 4 - exit")
#         while oper != 'exit':


