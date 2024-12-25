import pytest
from src.v2.thin_crust import ThinCrust
from src.v2.cheese import Cheese
from src.v2.sausage import Sausage
from src.v2.stuffed_crust import StuffedCrust
from src.v2.blackolive import BlackOlive
from src.v2.handtossedcrust import HandTossedCrust
from src.v2.deepdishcrust import DeepDishCrust
from src.v2.pepperoni import Pepperoni
from src.v2.pizza import Pizza


def test_thin_crust():
    pizza = ThinCrust()
    assert pizza.is_vegetarian() == True
    assert pizza.calculate_price() == 8.0


def test_thin_cheese():
    pizza = Cheese(ThinCrust())
    assert pizza.is_vegetarian() == True
    assert pizza.calculate_price() == 9.0


def test_stuffed_sausage():
    pizza = Sausage(StuffedCrust())
    assert pizza.is_vegetarian() == False
    assert pizza.calculate_price() == 9.50


def test_hand_tossed_veggie():
    pizza = BlackOlive(Cheese(BlackOlive(HandTossedCrust())))
    assert pizza.is_vegetarian() == True
    assert pizza.calculate_price() == 11.00


def test_remove_cheese():
    pizza = ThinCrust()
    pizza_without_cheese = pizza.remove_topping(Cheese)
    assert pizza is pizza_without_cheese


def test_remove_pepperoni():
    pizza = Cheese(Pepperoni(Cheese(Pepperoni(StuffedCrust()))))
    pizza_without_pepperoni = pizza.remove_topping(Pepperoni)
    assert pizza_without_pepperoni.is_vegetarian()
    assert pizza_without_pepperoni.calculate_price() == 10.0


def test_is_dairy_free_psych():
    pizza = Cheese(ThinCrust())
    assert not pizza.is_dairy_free()


def test_is_dairy_free():
    pizza = Pepperoni(DeepDishCrust())
    assert pizza.is_dairy_free()
