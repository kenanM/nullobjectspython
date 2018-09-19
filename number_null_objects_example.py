from optional import optional_of_nullable, optional_of, empty


def product(x, y):
    return x.get(default=0) * y.get(default=0)


def sum(x, y):
    return x.get(default=0) + y.get(default=0)
