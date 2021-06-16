from functools import wraps


def wrap_with_tag(tag):
    def decorator(func):
        @wraps(func)
        def inner(*args):
            result = func(*args)

            return f'<{tag}>{result}</{tag}>'

        return inner

    return decorator


@wrap_with_tag('b')
def return_hello_world():
    return 'Hello world'


print(return_hello_world())  # <b>Hello world</b>
print(return_hello_world.__name__)  # return_hello_world
