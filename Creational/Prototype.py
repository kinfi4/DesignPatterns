import copy
from collections import namedtuple


class Prototype:
    def __init__(self, some_int, some_list, some_obj):
        self.some_int = some_int
        self.some_list = some_list
        self.some_obj = some_obj

    def __copy__(self):
        """ This method evoke when someone use copy.copy on our object"""

        new_list = copy.copy(self.some_list)
        new_obj = copy.copy(self.some_obj)

        new = self.__class__(
            self.some_int, new_list, new_obj
        )

        new.__dict__.update(self.__dict__)

        return new

    def __deepcopy__(self, memo_dict={}):
        """ This method evoke when someone use copy.deepcopy on our object"""

        new_list = copy.deepcopy(self.some_list)
        new_obj = copy.deepcopy(self.some_obj)

        new = self.__class__(
            self.some_int, new_list, new_obj
        )

        new.__dict__ = copy.deepcopy(self.__dict__)

        return new


Klass = namedtuple('Klass', ['count'])

list_of_objects = [1, {1, 2, 3}, [1, 2, 3]]
obj = Klass(lambda self: print('Hello world'))

prototype = Prototype(10000, list_of_objects, obj)


prototype2 = copy.copy(prototype)
print(prototype2.some_int is prototype.some_int)  # True, I have no idea, seems like that`s some sort of optimization
print(prototype2.some_list is prototype.some_list)  # True
print(prototype2.some_obj is prototype.some_obj)  # True

print('=' * 30)

prototype2 = copy.deepcopy(prototype)
print(prototype2.some_int is prototype.some_int)  # True
print(prototype2.some_list is prototype.some_list)  # False
print(prototype2.some_obj is prototype.some_obj)  # False
