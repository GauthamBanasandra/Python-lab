__author__ = 'gauth_000'


def decorator(f):
    def inner_function(x):
        print('begin decoration')
        f(x)
        print('end decoration')

    return inner_function


@decorator
def some_function(x):
    print('inside some function', x)

print('calling some function')
some_function(1)
