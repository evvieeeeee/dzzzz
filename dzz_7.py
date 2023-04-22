from random import random
class RandomIncrease:
    def __init__(self, amount):
        self.amo = amount
        self.cur = 0

    def __iter__(self):
        return generator

    def random_increase(amount):
        cur = 0
        while amount > 0:
            cur += random()
            amount -= 1
            yield round(cur, 2)

    generator = random_increase(5)
    for i in generator:
        print(i)


