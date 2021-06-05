#  Идея в том чтоб разделить абстракцию и реализацию. Абстракция тут это не тоже что в проге, это просто
#  система, что делигирует свои задачи кому то еще. На пример: GUI - абстракция, API - реализация
#  (GUI просто делигирует).
#  Ну вот эти две штуки нужно разделить, так чтоб они были независимы. И можно было заменить одно на другое

from abc import ABC, abstractmethod


class API(ABC):
    @abstractmethod
    def calculate(self):
        pass


class FirstAPI(API):
    def calculate(self):
        return 'Result of calculations in FirstAPI'


class SecondAPI(API):
    def calculate(self):
        return 'Result of calculations in SecondAPI'


class GUI:
    def __init__(self, api: API):
        self.api = api

    def make_calculations(self):
        print(self.api.calculate())


gui1 = GUI(FirstAPI())
gui1.make_calculations()

gui2 = GUI(SecondAPI())
gui2.make_calculations()
