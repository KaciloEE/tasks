def fib(n):
    assert n >= 0
    return n if n <= 1 else fib(n-1) + fib(n-2)

print(fib(30))


cache = {}
def fib1(n):
    assert n >= 0
    if n not in cache:
        cache[n] = n if n <= 1 else fib1(n - 1) + fib1(n - 2)
    return cache[n]

print(fib1(30))


def fib2(n):
    assert n >= 0
    f0, f1 = 0, 1
    for i in range(n - 1):
        f0, f1 = f1, f0 + f1
    return f1

print(fib2(30))
