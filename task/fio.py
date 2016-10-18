#import sys

#a = sys.argv
a = ['dsf','kaka','sadasd','sdfsdf']

fio = a[1:]
fio_n = []

for i in fio:
  fio_n.append(i.capitalize())

print('{0} {1} {2}'.format(fio_n[0],fio_n[1],fio_n[2]))

print('{0} {1} {2}'.format(fio[0].capitalize(),fio[1].capitalize(),fio[2].capitalize()))







