from src.v2.pizza import Pizza


class BlackOlive(Pizza):

    def __init__(self, pizza):
        self.base = pizza

    def is_vegetarian(self):
        return self.base.is_vegetarian()

    def calculate_price(self):
        return 1.0 + self.base.calculate_price()
