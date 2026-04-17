# # OOP
# # 17 04 2026

# class User:
#     counter = 0  #  Переменная класа
#
#     def __init__(self, user_name, user_phone, user_email):
#         self.name = user_name
#         self.phone = user_phone
#         self.email = user_email
#         User.counter += 1
#
#
# u1 = User("Valera", "123", "llkjjj")
#
# u2 = User("Snnya", "456", "ppoiuy")
#
# print(u1.name)
#
# # Переменная класса
# print(User.counter)
# print(u2.counter)


# class User:
#     counter = 0  #  Переменная класа
#
#     def __init__(self, user_name, user_phone, age, user_email):
#         self.name = user_name
#         self.phone = user_phone
#         self.email = user_email
#         self.age = age
#         User.counter += 1
#
#     def get_name(self):
#         return self.name
#
#     def get_phone(self):
#         return self.phone
#
#     def get_email(self):
#         return self.email
#
#     def __str__(self):
#         return f'name: {self.name} | phone: {self.phone} | age: {self.age} | email: {self.email}'
#
#     def __repr__(self):
#         return f'repr name: {self.name} | phone: {self.phone} | email: {self.email}'
#
#     def __len__(self):
#         return self.age
#
# u1 = User("Valera", "123", 123, "llkjjj")
#
# # print(u1.get_name())
# # print(u1.get_phone())
# # print(u1.get_email())
#
# print(u1)
#
# print(len(u1))

# # Наследование
#
# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def speak(self, sound):
#         return f'{self.name} says {sound}'
#
#     def __repr__(self):
#         return f'{self.name} age {self.age}'
#
# class Bulldog(Dog):
#
#     def walk(self, steps):
#         return f'{self.name} walks {steps} steps'
#
#     def speak(self, sound):
#         return f'bulldog speaks  {sound}\n' + super().speak(sound)
#
# jimmy = Bulldog('Jimmy', 6)
#
# print(jimmy)
#
# print(jimmy.speak('гав-гав'))
#
# print(jimmy)
#
# print(Bulldog.__bases__)
#
# print(jimmy.walk(150))
#
# print(jimmy.speak('dsdds'))