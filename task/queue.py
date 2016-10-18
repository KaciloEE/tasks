file = open('queue.txt', 'r')

a = file.read()
b = a.split(' ')
b.sort()
b.reverse()

print(b)

print(sorted(a.split(' '), reverse=True))
