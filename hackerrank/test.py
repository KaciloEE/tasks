#n1 = int(input().strip())
#s1 = list(map(int,input().split()))
#n2 = int(input().strip())
#s2 = input().split()
s1 = [8,-10]
s2 = [5,6,7]
s1 = set(s1)
s2 = set(s2)

l = list(s1.symmetric_difference(s2))

for i in l:
    print(i)
