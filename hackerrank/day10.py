n = 65535
n = bin(n)[2:]
count = 0
c = []
if '0' in n:
  for i in n:
    if int(i)==1:
      count+=1
    else:
      c.append(count)
      count = 0
  c.append(count)
else:
  n = len(n)
  c.append(n)
print(max(c))


n = int(input().strip())
count = 0
maxi = 0
while n > 0:
    if n % 2 == 1:
        count += 1
    else:
        if count > maxi:
            maxi = count
        count = 0
    n=math.floor(n / 2)
if count > maxi:
    maxi = count
print(maxi)




