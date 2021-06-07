#  Вообще идя довольно проста, суть в том что когда у нас есть составные объекты и просто объекты вместе. Сделать
#   им общие интерфейсы.
#  Примером тут будет коробки заказов и продукты. В коробке может быть как другая коробка так и продукт, а задачей:
#   посчитать сумму заказа.

from abc import ABC, abstractmethod
from typing import List


class Item(ABC):
    @abstractmethod
    def calc_price(self):
        pass


class Box(Item):
    def __init__(self, children: List[Item]):
        self.children = children

    def calc_price(self):
        return sum([item.calc_price() for item in self.children])


class Commodity(Item):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def calc_price(self):
        return self.price


top_box = Box([Commodity('laptop', 200), Box([Commodity('phone', 100), Commodity('headphones', 300)])])

print(top_box.calc_price())  # 600
