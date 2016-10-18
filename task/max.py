import sys

n = sys.argv
x = n[1:]

for i, elem in enumerate(x):
    x[i] = int(elem)


print(max(x))
