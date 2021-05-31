from abc import ABC, abstractmethod


class PetFactory(ABC):
    @abstractmethod
    def get_pet(self, name):
        pass

    @abstractmethod
    def get_pet_food(self):
        pass


class Dog:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print('Dog says its name', self.name)


class Cat:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print('Cat says its name', self.name)


class DogFactory(PetFactory):
    def get_pet(self, name):
        return Dog(name)

    def get_pet_food(self):
        return 'Dog food'


class CatFactory(PetFactory):
    def get_pet(self, name):
        return Cat(name)

    def get_pet_food(self):
        return 'Cat food'


class PetStore:
    def __init__(self, pet_factory: PetFactory, pet_name: str):
        self._pet_factory = pet_factory
        self._pet_name = pet_name

    def show_pet(self):
        """Utility method printing the details of pet created using factory"""

        pet = self._pet_factory.get_pet(self._pet_name)
        pet_food = self._pet_factory.get_pet_food()

        pet.speak()
        print('Pet', pet.name, 'likes', pet_food)


store = PetStore(DogFactory(), 'Garic')
store.show_pet()

store = PetStore(CatFactory(), 'Alice')
store.show_pet()
