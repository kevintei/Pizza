from src.v2.pizza import Pizza


class DeepDishCrust(Pizza):

    def is_vegetarian(self):
        return True

    def calculate_price(self):
        return 8.0

    def is_dairy_free(self):
        return True
