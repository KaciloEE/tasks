import sys

n = int(input().strip())
#s = input()
#lst = list(map(int,s.split()))
lst = [int(x) for x in input().split()]
a = []
for i in set(lst):
  a.append(i)

a.sort()
print(a[-2])


