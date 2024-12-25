from src.v2.pizza import Pizza


class Pepperoni(Pizza):
    def __init__(self, pizza):
        self.base = pizza

    def is_vegetarian(self):
        return False

    def calculate_price(self):
        return 4.0 + self.base.calculate_price()

    def is_dairy_free(self):
        return True

    def remove_topping(self, topping):
        if isinstance(self, topping):
            return self.base.remove_topping(topping)
        return Pepperoni(self.base.remove_topping(topping))
