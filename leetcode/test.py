def hammingDistance(x, y):
    print(bin(x))
    print(bin(y))
    return bin(x^y).count('1')

print(hammingDistance(1,4))