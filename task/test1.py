s = "wowhatamanwowowpalehche"
s1 = 'wow'
l = []
for i in range(len(s)):
    n = s.find(s1, i)
    if n !=-1:
        l.append(n)

print(len(set(l)))


