import random

class Cat:
    def __init__(self, name):
        self.name = name
        self.hunger = 50
        self.energy = 50
        self.hapiness = 50
        self.alive = True

    def to_eat(self):
        print("Time to eat...")
        self.hunger += 20
        self.energy += 5
        if self.hunger < 0:
            self.hunger = 0
        if self.hunger > 100:
            self.hunger = 100

        if self.energy < 0:
            self.energy = 0
        if self.energy > 100:
            self.energy = 100

        if self.hapiness < 0:
            self.hapiness = 0
        if self.hapiness > 100:
            self.hapiness = 100

    def to_sleep(self):
        print("Time to sleep...")
        self.energy += 40
        self.hunger += 10
        if self.hunger < 0:
            self.hunger = 0
        if self.hunger > 100:
            self.hunger = 100

        if self.energy < 0:
            self.energy = 0
        if self.energy > 100:
            self.energy = 100

        if self.hapiness < 0:
            self.hapiness = 0
        if self.hapiness > 100:
            self.hapiness = 100

    def to_play(self):
        print("Time to play...")
        self.hapiness += 20
        self.energy -= 15
        self.hunger -= 10
        if self.hunger < 0:
            self.hunger = 0
        if self.hunger > 100:
            self.hunger = 100

        if self.energy < 0:
            self.energy = 0
        if self.energy > 100:
            self.energy = 100

        if self.hapiness < 0:
            self.hapiness = 0
        if self.hapiness > 100:
            self.hapiness = 100

    def is_alive(self):
        if self.hunger <= 0:
            print("Starvation...")
            self.alive = False
        elif self.energy <= 0:
            print("Exhale...")
            self.alive = False
        elif self.hapiness <= 0:
            print("Depression..")
            self.alive = False
        elif self.hunger > 0 and self.energy > 0 and self.hapiness > 0:
            print("Survived...")

    def end_of_day(self):
        print(f"Hunger = {self.hunger}")
        print(f"Energy = {self.energy}")
        print(f"Hapiness = {self.hapiness}")

    def live(self, day):
        day = "Day" + str(day) + " of " + self.name + "life"
        print(f"{day:=^50}")
        live_cube = random.randint(1, 4)
        if live_cube == 1:
            self.to_eat()
        elif live_cube == 2:
            self.to_sleep()
        elif live_cube == 3:
            self.to_play()
        elif live_cube == 4:
            print("Just chilling...")
            self.hunger -= 5
            self.energy += 5
        self.end_of_day()
        self.is_alive()

nick = Cat(name = "Oscar ")
for day in range(365):
    if nick.alive == False:
        break
    nick.live(day)