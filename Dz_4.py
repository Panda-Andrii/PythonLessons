class Character:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        print(f"{self.name} створений з HP {self.hp}")

    def attack(self):
        print("Персонаж атакує!")


class Warrior(Character):
    def __init__(self, name, hp, weapon):
        super().__init__(name, hp)
        self.weapon = weapon

    def attack(self):
        super().attack()
        print(f"Атакує з допомогою: {self.weapon}")


class Barbarion(Warrior):
    def __init__(self, name, hp, weapon):
        super().__init__(name, hp, weapon)

    def attack(self):
        Character.attack(self)
        print(f"Вибігає з {self.weapon}")


class Paladin(Warrior):
    def __init__(self, name, hp, shield):
        super().__init__(name, hp, shield)
        self.shield = shield

    def attack(self):
        Character.attack(self)
        print(f"Захищає за допомогою {self.shield}")


class Mage(Character):
    def __init__(self, name, hp, magic):
        super().__init__(name, hp)
        self.magic = magic

    def attack(self):
        super().attack()
        print(f"Кастує заклинання {self.magic}")


class Necromancer(Mage):
    def __init__(self, name, hp, magic):
        super().__init__(name, hp, magic)

    def attack(self):
        Character.attack(self)
        print(f"Некромант піднімає мертвих за допомгою {self.magic}")

class Druid(Mage):
    def __init__(self, name, hp, magic):
        super().__init__(name, hp, magic)

    def attack(self):
        Character.attack(self)
        print(f"Друїд піднімає лози за допомгою {self.magic}")


class Archer(Character):
    def __init__(self, name, hp, bow):
        super().__init__(name, hp)
        self.weapon = bow

    def attack(self):
        super().attack()
        print(f"Стріляє з {self.weapon}")


class Assasin(Archer):
    def __init__(self, name, hp, knife):
        super().__init__(name, hp, knife)

    def attack(self):
        Character.attack(self)
        print(f"Приховано нападає з {self.weapon}")

class Rogue(Archer):
    def __init__(self, name, hp, knife):
        super().__init__(name, hp, knife)

    def attack(self):
        Character.attack(self)
        print(f"Підкрадується з {self.weapon}")


def select_warrior():
    print("Оберіть підклас:")
    print("1 = Warrior")
    print("2 = Barbarion")
    print("3 = Paladin")

    choice = input("Ваш вибір: ")
    if choice == "1":
        return Warrior("Фауст", 100, "Меч")
    elif choice == "2":
        return Barbarion("Шерлок", 120, "Сокира")
    elif choice == "3":
        return Paladin("Флор", 140, "Щит")
    else:
        print("Неправильний вибір!")
        return select_warrior()


def select_mage():
    print("Оберіть підклас:")
    print("1 = Mage")
    print("2 = Necromancer")
    print("3 = Druid")

    choice = input("Ваш вибір: ")
    if choice == "1":
        return Mage("Мерлін", 90, "Вогонь")
    elif choice == "2":
        return Necromancer("Потап", 70, "Призив тьми")
    elif choice == "3":
        return Druid("Вербан", 100, "Призив природи")
    else:
        print("Неправильний вибір!")
        return select_mage()


def select_archer():
    print("Оберіть підклас:")
    print("1 = Archer")
    print("2 = Assasin")
    print("3 = Rogue")

    choice = input("Ваш вибір: ")
    if choice == "1":
        return Archer("Троєць", 90, "Лук")
    elif choice == "2":
        return Assasin("Шаміль", 70, "Метальні ножі")
    elif choice == "3":
        return Rogue("Щек", 80, "Арбалет")
    else:
        print("Неправильний вибір!")
        return select_archer

def start_game():
    print("Вітаю! Вибери свій клас:")
    print("1 - Воїни\n2 - Маги\n3 - Лучник")

    category = input("Ваш вибір: ")
    player = None

    if category == "1":
        player = select_warrior()
    elif category == "2":
        player = select_mage()
    elif category == "3":
        player = select_archer()
    else:
        print("Неправильний вибір!")
        return start_game()

    if player:
        print("------ Ви обрали героя! ------")
        player.attack()

start_game()