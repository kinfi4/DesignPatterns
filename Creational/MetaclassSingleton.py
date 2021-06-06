class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)

        return cls._instances[cls]


class SomeClass(metaclass=Singleton):
    pass


if __name__ == '__main__':
    s1 = SomeClass()
    s2 = SomeClass()

    print(s1 is s2)  # True
