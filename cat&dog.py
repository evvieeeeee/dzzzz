import random
class Dog:
    def __init__(self, name):
        self.name = name
        self.health = 0
        self.gladness = 50
        self.alive = True

    def to_walk(self):
        print("Time to walk")
        self.gladness += 10
        self.health += 5


    def to_sleep(self):
        print("Let's go sleep")
        self.gladness += 5
        self.health += 1


    def to_being_treated(self):
        print("We have to go to the doctor")
        self.gladness -= 15
        self.health += 10

    def to_play(self):
        print("I want to play")
        self.gladness += 10
        self.health -= 5

    def is_alive(self):
        if self.health < 4:
            print("I feel bad..")
            self.to_being_treated()
            self.alive = False
        elif self.gladness <= 10:
            print("I'm sad but healthy")
            self.alive = False
        elif self.health > 10:
            print("Everything is OK")
            self.alive = True

    def end_of_day(self):
        print(f"Gladness = {self.gladness}")
        print(f"Health = {round(self.health, 2)}")

    def live(self, day):
        day = "Day" + str(day) + "of" + self.name + "'s" + "life"
        print(f"{day:=^50}")

        live_cube = random.randint(1, 3)

        if live_cube == 1:
            self.to_walk()
        elif live_cube == 2:
            self.to_play()
        elif live_cube == 3:
            self.to_sleep()

         self.end_of_day()
        self.is_alive()

dog = Dog(name="Chennie")

for day in range(365):
    if dog.alive:
        dog.live(day)