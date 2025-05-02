# prototype.py

import copy

class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def clone(self):
        return copy.deepcopy(self)

    def __str__(self):
        return f"{self.name} - ${self.price}"
