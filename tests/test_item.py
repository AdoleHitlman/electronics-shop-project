"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item

item1 = Item("Смартфон", 10000, 20)
Item.pay_rate = 0.8


def test_pay_rate():
    assert item1.pay_rate == 0.8


def test_name():
    assert item1.name == "Смартфон"


def test_price():
    assert item1.price == 10000


def test_quantity():
    assert item1.quantity == 20


def test_calculate_total_price():
    assert item1.calculate_total_price() == 200000


def test_apply_discount():
    assert item1.apply_discount() == None
