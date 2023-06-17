"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item
import pytest

item1 = Item("Смартфон", 10000, 20)
Item.pay_rate = 0.8


def test___repr__():
    assert item1.__repr__() == "Смартфон,('Смартфон', 10000, 20)"


def test___str__():
    assert item1.__str__() == "Смартфон"


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


def test_name_property():
    item = Item('Телефон', 10000, 5)

    # длина наименования товара меньше 10 символов
    item.name = 'Смартфон'
    assert item.name == 'Смартфон'

    # длина наименования товара больше 10 символов
    with pytest.raises(ValueError):
        item.name = 'СуперСмартфон'


def test_instantiate_from_csv():
    Item.instantiate_from_csv()
    assert len(Item.all) == 5  # в файле 5 записей с данными по товарам

    item1 = Item.all[0]
    assert item1.name == 'Смартфон'


def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5

def test___add__():
    item = Item("iPhone 13", 120_000, 5)
    assert item.__add__(item) == 10