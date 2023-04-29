from random import random
class RandomIncrease:
    def __init__(self, amount):
        self.i = 0
        self.amount = amount

    def __iter__(self):
        self.i = 0
        yield self

    def random_increase(self):
        cur = 0
        while self > 0:
            cur += random()
            self -= 1
            yield round(cur, 2)

    generator = random_increase(5)
    for i in generator:
        print(i)


