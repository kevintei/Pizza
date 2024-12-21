from src.v2.pizza import Pizza

class Cheese(Pizza):
    def __init__(self, pizza):
        self.base = pizza
    def is_veggetarian(self):
        return self.base.is_veggetarian()
    def calculate_price(self):
        return(1.0 + self.base.calculate_price())