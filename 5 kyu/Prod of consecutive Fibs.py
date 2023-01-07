def productFib(prod):
    a = 0
    b = 1
    while a*b < prod:
        b = a + b
        a = b - a
    return [a, b, True] if a*b == prod else [a, b, False]
