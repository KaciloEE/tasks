a = [input().split() for i in range(int(input()))]
name = input().strip()

for i in (x[0] for x in a if x[0] == name):
  print(a[i])

