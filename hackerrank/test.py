s = 'AABAACAAD'
s1=[]
n = 0
n1 =3
while len(s)<9:
  s1.append(s[n:n1])
  n+=3
  n1+=3


print(s1)
