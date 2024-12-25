from src.v2.pizza import Pizza


class HandTossedCrust(Pizza):
    def is_vegetarian(self):
        return True

    def calculate_price(self):
        return 8.0
