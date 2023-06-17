from src.phone import Phone
import pytest


def test_phone_init():
    phone = Phone("iPhone 13", 120_000, 5, 2)
    assert phone.name == "iPhone 13"
    assert phone.price == 120_000
    assert phone.quantity == 5
    assert phone.number_of_sim == 2


def test_invalid_number_of_sim():
    with pytest.raises(TypeError):
        phone = Phone("iPhone 13", 120_000, 5, -1)

def test_add_items():
    phone = Phone("iPhone 13", 120_000, 5, 2)
    assert phone.__add__(phone) == 10

def test_repr():
    phone = Phone("iPhone 13", 120_000, 5, 2)
    assert repr(phone) == "Phone('iPhone 13', 120000, 5, 2)"