class Dog:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print('Woof! From', self.name)


class Cat:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print('Meow! From', self.name)


def get_pet(pet_name, pet='dog'):
    """The Factory Method"""

    pets = {'dog': Dog(pet_name), 'cat': Cat(pet_name)}

    if pet not in pets:
        raise ValueError('Cant create a pet with type:', pet)

    return pets[pet]


get_pet('Garik').speak()
get_pet('Alice', 'cat').speak()
