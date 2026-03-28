

"""
class Animal:
    def __init__(self, name):
        self.name = name
        print(f"Тварина {self.name} створена!")

    def speak(self):
        print("Тварина видає звук")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
        self.breed = (f"Собака породи {self.breed} створений!")
    def speak(self):
        super().speak()
        print("Гав, гав!")

class Cat(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
        self.breed = (f"Кот породи {self.breed} створений!")
    def speak(self):
        super().speak()
        print("Мяу, мяу!")

dog = Dog("Арчі", "Боксер")
cat = Cat("Хорст", "Турецька ангора")
cat.speak()
dog.speak()
"""

class Character:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        print(f"{self.name} ствоорений з HP {self.hp}")
    def attack(self):
        print("Персонаж атакує!")

class Warrior(Character):
    def __init__(self, name, hp, weapon):
        super().__init__(name, hp)
        self.weapon = weapon

    def attack(self):
        super().attack()
        print(f"Атакує {self.weapon}")

class Mage(Character):
    def __init__(self, name, hp, magic):
        super().__init__(name, hp)
        self.magic = magic

    def attack(self):
        super().attack()
        print(f"Кастує заклинання {self.magic}")

class Spearman(Character):
    def __init__(self, name, hp, spear):
        super().__init__(name, hp)
        self.spear = spear

    def attack(self):
        super().attack()
        print(f"Вбігає з {self.spear}")

w = Warrior("Артур", 100, "Меч")
m = Mage("Мерлін", 80, "Вогонь")
s = Spearman("Троєць", 90, "Загостериний спис")

w.attack()
m.attack()
s.attack()

