import sys

n = sys.argv[1]

mw = list(n)
m=mw.count('m')
w=mw.count('w')
s = '*' * m
ss = '*' * w

print('m  {0} {1}'.format(m,s) )
print('w  {0} {1}'.format(w,ss) )
