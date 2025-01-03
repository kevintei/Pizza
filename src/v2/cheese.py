from src.v2.pizza import Pizza


class Cheese(Pizza):
    def __init__(self, pizza):
        self.base = pizza

    def is_vegetarian(self):
        return self.base.is_vegetarian()

    def calculate_price(self):
        return 1.0 + self.base.calculate_price()

    def is_dairy_free(self):
        return False

    def remove_topping(self, topping):
        if isinstance(self, topping):
            return self.base.remove_topping(topping)
        return Cheese(self.base.remove_topping(topping))
