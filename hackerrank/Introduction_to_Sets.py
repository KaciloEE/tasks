import sys

n = int(input().strip())
s = set(list(map(int, input().split())))

print(sum(s) / len(s))
