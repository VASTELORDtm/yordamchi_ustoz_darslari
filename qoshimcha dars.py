# class BankAccount:
#     def __init__(self, account_number, initial_balance=0):
#         self.account_number = account_number
#         self._balance = initial_balance
#
#     @property
#     def balance(self):
#         return self._balance
#
#     def deposit(self, amount):
#         if amount > 0:
#             self._balance += amount
#             print(f"{amount} so'm depozit qilindi. Yangi balans: {self._balance} so'm.")
#         else:
#             print("Iltimos, musbat miqdorda depozit qiling.")
#
#     def withdraw(self, amount):
#         if 0 < amount <= self._balance:
#             self._balance -= amount
#             print(f"{amount} so'm yechildi. Yangi balans: {self._balance} so'm.")
#         else:
#             print("Yechish uchun yetarli mablag' yo'q yoki noto'g'ri miqdor kiritildi.")
#
# account = BankAccount("998810120", 1000)
# print(account.balance)
#
# account.deposit(500)
# print(account.balance)
#
# account.withdraw(200)
# print(account.balance)
#
# account.withdraw(1500)
# class Animal:
#     def sound(self):
#         raise NotImplementedError("Bu metod har bir hayvon turi uchun amalga oshirilishi kerak.")
#
#     def speed(self):
#         raise NotImplementedError("Bu metod har bir hayvon turi uchun amalga oshirilishi kerak.")
#
#     def characteristics(self):
#         raise NotImplementedError("Bu metod har bir hayvon turi uchun amalga oshirilishi kerak.")
#
#
# class Cat(Animal):
#     def sound(self):
#         return "Miyau"
#
#     def speed(self):
#         return "Tezligi: 30 km/s"
#
#     def characteristics(self):
#         return "Mushuklar mustaqil va o'z-o'zini parvarish qiladigan hayvonlardir."
#
#
# class Dog(Animal):
#     def sound(self):
#         return "woof"
#
#     def speed(self):
#         return "Tezligi: 40 km/s"
#
#     def characteristics(self):
#         return "Itlar sodiq va do'stona hayvonlardir."
#
#
# class Bird(Animal):
#     def sound(self):
#         return "Qaaaaar"
#
#     def speed(self):
#         return "Tezligi: 50 km/s"
#
#     def characteristics(self):
#         return "Qushlar uchish qobiliyatiga ega va turli ranglar bilan ajralib turadi."
#
#
# def animal_info(animal):
#     print(f"Tovushi: {animal.sound()}")
#     print(animal.speed())
#     print(animal.characteristics())
#     print()
#
#
# cat = Cat()
# dog = Dog()
# bird = Bird()
#
# animal_info(cat)
# animal_info(dog)
# animal_info(bird)
# class Book:
#     def __init__(self, title, author, price):
#         self.title = title
#         self.author = author
#         self._price = price
#
#     @property
#     def price(self):
#         return self._price
#
#     def update_price(self, new_price):
#         if new_price >= 0:
#             self._price = new_price
#             print(f"{self.title} narxi {new_price} so'mga yangilandi.")
#         else:
#             print("Narx musbat bo'lishi kerak.")
#
#     def display_info(self):
#         print(f"Kitob nomi: {self.title}, Muallif: {self.author}, Narxi: {self._price} so'm")
#
# book1 = Book("O'tkan kunlar", "Abdulla Qodiriy", 15000)
# book1.display_info()
#
# book1.update_price(20000)
# book1.display_info()
#
# book1.update_price(25000)
