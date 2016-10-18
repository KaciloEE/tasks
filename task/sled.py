f = open('matrix.txt', 'r')
m = f.read()
m = m.split('\n')

s1 = m[0].split(' ')
s2 = m[1].split(' ')
s3 = []
s3.append(s1)
s3.append(s2)
s4 = []
i=0
while i < len(s3):
  s4.append(s3[i][i])
  i += 1

s5 = 0
for i in s4:
  s5 +=int(i)

print(s5)

