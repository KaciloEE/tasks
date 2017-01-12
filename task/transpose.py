f = open('transpose_matrix.txt', 'w')
m = [['1','2'],['3','4'],['5','6']]
l1 = []
l2 = []

for i in m:
  l1.append(i[0])
  l2.append(i[1])

f.write(" ".join(l1))
f.write('\n'+ " ".join(l2))
