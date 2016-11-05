a = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]
size=int(len(a))

s1 = []
s2 = []
for i in range(len(a)):
    s1.append(a[i][i])

for i in range(len(a)):
    s2.append(a[i][(size-1)-i])

    
    
print(abs(sum(s1)-sum(s2)))
#test

