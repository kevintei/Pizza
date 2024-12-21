import pytest
from src.v2.thin_crust import ThinCrust
from src.v2.cheese import Cheese

def test_thin_crust():
    pizza = ThinCrust()
    assert(pizza.is_veggetarian() == True)
    assert(pizza.calculate_price() == 8.0)

def test_thin_cheese():
    pizza = Cheese(ThinCrust())
    assert(pizza.is_veggetarian() == True)
    assert(pizza.calculate_price() == 9.0)

def test_stuffed_sausage():
    pizza = Sausage(StuffedCrust())
    assert(pizza.is_veggetarian() == False)
    assert(pizza.calculate_price() == 9.50)

def test_hand_tossed_veggie():
    pizza = BlackOlive(Cheese(BlackOlive(HandTossedCrust())))
    assert(pizza.is_veggetarian() == True)
    assert(pizza.calculate_price() == 11.00)

def test_remove_cheese():
    pizza = ThinCrust()
    pizza_without_cheese = pizza.remove_topping(Cheese)
    assert(pizza is pizza_without_cheese)

def test_remove_pepperoni():
    pizza = Cheese(Pepperoni(Cheese(Pepperoni(StuffedCrust()))))
    pizza_wihout_pepperoni = pizza.remove_topping(Pepperoni)
    assert(pizza_wihout_pepperoni.is_veggetarian())
    assert(pizza_wihout_pepperoni.calculate_price() == 10.0)

def test_is_dairy_free_psych():
    pizza = Cheese(ThinCrust())
    assert(not pizza.is_dairy_free())

def test_is_diary_free():
    pizza = Pepperoni(DeepDishCrust())
    assert(pizza.is_dairy_free())