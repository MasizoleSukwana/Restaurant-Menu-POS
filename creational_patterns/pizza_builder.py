# pizza_builder.py

class Pizza:
    def __init__(self):
        self.ingredients = []

    def add(self, ingredient):
        self.ingredients.append(ingredient)

    def describe(self):
        return f"Pizza with: {', '.join(self.ingredients)}"

class PizzaBuilder:
    def __init__(self):
        self.pizza = Pizza()

    def add_cheese(self):
        self.pizza.add("cheese")
        return self

    def add_pepperoni(self):
        self.pizza.add("pepperoni")
        return self

    def add_mushrooms(self):
        self.pizza.add("mushrooms")
        return self

    def build(self):
        return self.pizza
