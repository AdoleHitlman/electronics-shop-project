import csv


class InstantiateCSVError(Exception):
    pass


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)
        super().__init__()

    def __add__(self, other):
        if isinstance(other, Item):
            return self.quantity + other.quantity
        else:
            raise ValueError("Невозможно сложить товары разных типов")

    """
        Магический метод __repr__
    """

    def __repr__(self):
        return f"{self},('{self.name}', {self.price}, {self.quantity})"

    """
    Магический метод __str__
    """

    def __str__(self):
        return self.name

    @property
    def name(self):
        """
        Геттер для доступа к приватному атрибуту name.
        """
        return self.__name

    @name.setter
    def name(self, value):
        """
        Сеттер для доступа к приватному атрибуту name.

        :param value: Новое значение для name.
        """
        if len(value) <= 10:
            self.__name = value
        else:
            raise ValueError('Длина наименования товара превышает 10 символов.')

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * self.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        """
        Создание экземпляров класса Item из данных файла src/items.csv.
        """
        cls.all = []
        try:
            with open('/home/hw/hw010623/electronics-shop-project/src/items.csv') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    if all([row['name'], row['price'], row['quantity']]):
                        item = cls(row['name'], float(row['price']), int(row['quantity']))
                        cls.all.append(item)
                    else:
                        raise InstantiateCSVError("Файл  item.csv поврежден")
        except FileNotFoundError:
            print("Отсутствует файл item.csv")
        except KeyError:
            raise InstantiateCSVError("Файл item.csv поврежден")

    @staticmethod
    def string_to_number(string) -> int:
        """
        Преобразует строку в число. Если число с плавающей точкой, возвращает целую часть.

        :param string: Число в виде строки.
        :return: Целое число.
        """
        return int(float(string))
