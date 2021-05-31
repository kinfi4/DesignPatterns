from abc import ABC, abstractmethod


class AbstractHouseBuilder(ABC):
    """ This class has all necessary method for building houses """

    @abstractmethod
    def build_roof(self):
        pass

    @abstractmethod
    def build_basement(self):
        pass

    @abstractmethod
    def build_walls(self):
        pass

    @abstractmethod
    def return_house(self):
        pass


class BuildModernHouse(AbstractHouseBuilder):
    def __init__(self):
        self.house = ModernHouse()

    def build_basement(self):
        self.house.add('modern basement')

    def build_walls(self):
        self.house.add('modern walls')

    def build_roof(self):
        self.house.add('modern roof')

    def return_house(self):
        return self.house


class BuildOldHouse(AbstractHouseBuilder):
    def __init__(self):
        self.house = OldHouse()

    def build_roof(self):
        self.house.add('old roof')

    def build_basement(self):
        self.house.add('old basement')

    def build_walls(self):
        self.house.add('old walls')

    def return_house(self):
        return self.house


class ModernHouse:
    def __init__(self):
        self._parts = []

    def add(self, part):
        self._parts.append(part)

    def __str__(self):
        return f'Modern House with: {self._parts}'


class OldHouse:
    def __init__(self):
        self._parts = []

    def add(self, part):
        self._parts.append(part)

    def __str__(self):
        return f'Old House with: {self._parts}'


class Director:
    """ Class controller, that controls the building of objects """

    def __init__(self, builder: AbstractHouseBuilder):
        self.builder = builder

    def build_full_house(self):
        self.builder.build_walls()
        self.builder.build_roof()
        self.builder.build_basement()

        return self.builder.return_house()


modern_director = Director(BuildModernHouse())
print(modern_director.build_full_house())

old_director = Director(BuildOldHouse())
print(old_director.build_full_house())