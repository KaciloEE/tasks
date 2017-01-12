a = "ambulance"
print(a[::-1])

l = [i for i in range(1,6)]

index = len(l)
s = []
while index:
    index-=1
    s.append(l[index])

print("".join(map(str,s)))

for i in s:
    print(i,end='')


