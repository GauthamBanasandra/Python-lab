__author__ = 'gauth_000'


def decorate_star(f):
    def inner(message):
        print('*' * len(message))
        f(message)
        print('*' * len(message))

    return inner


def decorate_dollar(f):
    def inner(message):
        print('$' * len(message))
        f(message)
        print('$' * len(message))

    return inner


@decorate_dollar
@decorate_star
def print_message(message):
    print(message)


print_message('decorator')
