class Ukrainian:
    def speak_ukrainian(self):
        print('Пішов у дупу')


class Russian:
    def speak_russian(self):
        print('Пошел в жопу')


class Adapter:
    def __init__(self, obj, **kwargs):
        self._object = obj
        self.__dict__.update(kwargs)

    def __getattr__(self, item):
        return getattr(self._object, item)


def client_code(people: list):
    for person in people:
        person.speak()


russian = Russian()
ukrainian = Ukrainian()

#  Идея тут в том, что у наших классов нет метода speak, но нам очень хочется его. Поэтому мы создали такой вот
#  класс Adapter, что принимает наш объект и словарь методов что мы хотим добавить в него
people = [Adapter(russian, speak=russian.speak_russian), Adapter(ukrainian, speak=ukrainian.speak_ukrainian)]

client_code(people)
