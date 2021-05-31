class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not isinstance(cls._instance, cls):
            cls._instance = super().__new__(cls, *args, **kwargs)

        return cls._instance


class MyClass(Singleton):
    pass


obj1 = MyClass()
obj2 = MyClass()

print(obj1 is obj2)
