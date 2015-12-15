__author__ = 'gauth_000'


class decorator:
    def __init__(self, f):
        print('init decorator')
        self.f=f

    def __call__(self, *args):
        print('inside call decorator')
        self.f(*args)

@decorator
def some_function(*x):
    print('in some function', x)

print('calling function now')
some_function(1, 2)
