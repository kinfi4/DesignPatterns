#  Тут идея в том чтоб создать цепочку handler-ов, каждый принимает запрос и решает, сможет ли он обработать его
#  если нет то передает запрос дальше. Что то вроде chain of middleware в ASP.NET CORE

#  Еще примером можно выделить django middleware, это тоже цепочка обязаностей.
#  Например, кода мы чекаем, авторизован ли пользователь, чтоб перейти на страницу.

from abc import ABC


class AbstractHandler(ABC):
    _next_handler = None

    def handle(self, request):
        if self._next_handler:
            return self._next_handler.handle(request)

        return None

    def set_next(self, handler):
        self._next_handler = handler
        return handler


class MonkeyHandler(AbstractHandler):
    def handle(self, request):
        if 'banana' in request:
            return f'Monkey ate {request}'

        return self._next_handler.handle(request)


class SquirrelHandler(AbstractHandler):
    def handle(self, request):
        if 'nut' in request:
            return f'Squirrel ate {request}'

        return self._next_handler.handle(request)


class DefaultHandler(AbstractHandler):
    def handle(self, request):
        return f'Dania ate {request}'


# build the handlers
monkey_handler, squirrel_handler, default_handler = MonkeyHandler(), SquirrelHandler(), DefaultHandler()

# build the chain
monkey_handler.set_next(squirrel_handler).set_next(default_handler)

requests = ['banana', 'banana with jem', 'nuts of your girl', 'cock']
for req in requests:
    print(monkey_handler.handle(req))
