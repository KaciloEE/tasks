def nod(a, b):
    while a and b:
        if a > b:
            a %= b
        else:
            b %= a
    return max(a, b)

print(nod(30,18))


def nod1(a, b):
    assert a >= 0 and b >= 0
    if a == 0 or b == 0:
        return max(a, b)
    return nod1(b % a, a)

print(nod1(30,18))
