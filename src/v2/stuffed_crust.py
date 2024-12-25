from src.v2.pizza import Pizza


class StuffedCrust(Pizza):
    def is_vegetarian(self):
        return True

    def calculate_price(self):
        return 8.0

    def remove_topping(self, topping_class):
        return self
