# Завдання 2: Робота з об'єктами
# Створіть клас `Rectangle`, який представляє прямокутник. Кожен об'єкт класу `Rectangle` повинен мати наступні атрибути:
# - `width` (ширина прямокутника)
# - `height` (висота прямокутника)
# Створіть конструктор класу, який ініціалізує ці атрибути при створенні об'єкта. 
# Напишіть метод `calculate_area()`, який розраховує площу прямокутника (площа = ширина * висота).
# Створіть два об'єкта класу `Rectangle` з різними розмірами та викличте їхні методи `calculate_area()`, 
# виведіть площу прямокутників на екран.

class Rectangle:
    """class Rectangle"""
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height
    
    def calculate_area(self):
        if self.width <= 0 or self.height <= 0:
            print(f"Width = {self.width}, Height = {self.height}")
            print("Error! Cannot calculate area when side value is less than 0")
        else:
            area = self.height * self.width
            print(f"Area of Rectangle (width = {self.width}, height = {self.height}) is {area}")

rectangle_01 = Rectangle(2, 5)
rectangle_01.calculate_area()

rectangle_01 = Rectangle(-2, 5)
rectangle_01.calculate_area()