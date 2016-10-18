file1 = open('shoopping_list_1.txt', 'r')
file2 = open('shoopping_list_2.txt', 'r')
file3 = open('shoopping_list_3.txt', 'r')

file_my = open('shoopping_list.txt', 'w')

file = file1.read().split('\n')
file += file2.read().split('\n')
file += file3.read().split('\n')

file_new = []
for i in set(file):
  file_new.append(i)

for item in sorted(file_new, reverse=True):
  file_my.write(item + '\n')
  file_my.close

print('Список покупок успешно создан...')





