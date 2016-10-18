f = open('numbers.txt', 'r')
n = f.read()
n = n.split(' ')
sum = 0

for i in n:
  if int(i)<0:
    sum +=int(i)

print(sum)


