cache = {}


def fib(n):
    assert n >= 0
    if n not in cache:
        cache[n] = n if n <= 1 else fib(n - 1) + fib(n - 2)
    return cache[n]

print(fib(30))
