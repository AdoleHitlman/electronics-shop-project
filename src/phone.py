from .item import Item

class Phone(Item):
    def __init__(self, name, price, quantity, number_of_sim):
        super().__init__(name, price, quantity)
        if number_of_sim <= 0:
            raise TypeError("ValueError: Количество физических SIM-карт должно быть целым числом больше нуля.")
        self.number_of_sim = number_of_sim


    def __add__(self, other):
        if isinstance(other, Item):
            return self.quantity + other.quantity
        elif isinstance(other, Phone):
            return self.quantity + other.quantity
        else:
            raise ValueError("Невозможно сложить товары разных типов")

    def __repr__(self):
        return f"Phone('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"