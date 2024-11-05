# Завдання 1: Створення класу і об'єктів
# Створіть клас `Animal`, який представляє тварину. Кожний об'єкт класу `Animal` повинен мати наступні атрибути:
# - `name` (ім'я тварини)
# - `species` (вид тварини)
# - `age` (вік тварини)
# Створіть конструктор класу, який ініціалізує ці атрибути при створенні об'єкта. 
# Напишіть метод `make_sound()`, який буде виводити звук, який виділяє тварина.
# Створіть два об'єкта класу `Animal` з різними характеристиками та викличте їхні методи `make_sound()`.

class Animal:
    """Class Animal"""
    def __init__(self, name, species, age) -> None:
        self.name = name
        self.species = species
        self.age = age

    def make_sound(self):
        if self.species == "dog":
            print("Dogs say 'Hav-Hav-Hav'")
        elif self.species == "cat":
            print("Cats say 'Miau-Miau-Miau'")
        elif self.species == "cow":
            print("Cows say 'Muuuuu-Muuuuu'")
        elif self.species == "horse":
            print("Horses say 'Ihoho'")
        elif self.species == "pig":
            print("Pigs say 'Khriu-Khriu'")
        else:
            print(f"Sorry! We do not know how {self.species} says")

animal_01 = Animal("Rocky", "dog", 3)
animal_02 = Animal("Marta", "cow", 2)
animal_03 = Animal("Sloneniatko", "elephant", 10)

animal_01.make_sound()
animal_02.make_sound()
animal_03.make_sound()