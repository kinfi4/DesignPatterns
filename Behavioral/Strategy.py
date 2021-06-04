import types


class RouteBuilder:
    """ This class represents map route builder, that can find out the easies way for us to get to the destination """

    def __init__(self, function=None):
        if function:
            self.build_route = types.MethodType(function, self)

    def build_route(self):
        raise NotImplementedError()


def walk_route(self):
    print('Build route for walk')


def bus_route(self):
    print('Build route for bus')


strategy_1 = RouteBuilder(walk_route)
strategy_2 = RouteBuilder(bus_route)

strategy_1.build_route()
strategy_2.build_route()
