n = 17
x = len(bin(n)[2:])
width = len("{0:b}".format(n))

for i in range(1,n+1):
  print(i, oct(i)[2:].rjust(x),hex(i)[2:].rjust(x),bin(i)[2:].rjust(x))



print(width)
