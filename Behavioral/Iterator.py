#  Идея в том, чтоб вынести алгоритм итерации по коллекции в отдельный класс,
#  вообще в пайтоне по другому и нельзя :З
#  Идея тут в том, что если завтра нам нужно будет как то по другому обойти нашу коллекцию, то мы просто
#  создадим еще один класс Iterator.

from collections.abc import Iterable, Iterator
from random import choice
from typing import Type


class StraightIterator(Iterator):
    def __init__(self, collection):
        self.collection = collection
        self.pos = 0

    def __next__(self):
        try:
            value = self.collection[self.pos]
            self.pos += 1
        except IndexError:
            raise StopIteration()

        return value

    def __iter__(self):
        return self


class RandomIterator(Iterator):
    def __init__(self, collection):
        self.collection = collection
        self.available_indexes = list(range(len(collection)))

    def __next__(self):
        if len(self.available_indexes) == 0:
            raise StopIteration()

        random_index = choice(self.available_indexes)
        self.available_indexes.remove(random_index)
        return self.collection[random_index]

    def __iter__(self):
        return self


class MyList(Iterable):
    def __init__(self, items, iterator: Type[Iterator] = StraightIterator):
        self.items = items
        self.iterator = iterator

    def __iter__(self):
        return self.iterator(self.items)


for item in MyList([4, 5, 6, 23, 3, 23, 123, 4, 5, 6]):
    print(item, end=' ')

print()

for item in MyList([4, 5, 6, 23, 3, 23, 123, 4, 5, 6], iterator=RandomIterator):
    print(item, end=' ')
