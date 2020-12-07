
def sum(a, b):
    print(a+b)


def subtract(a, b):
    print(a-b)


def difference(a,b):
    if a<b:
        a, b = b, a
    print(a-b)


def product(a, b):
    print(a*b)


def divide(a, b):
    print(a/b)


def real_divide(a, b):
    if a < b:
        a, b = b, a
    print(a/b)
