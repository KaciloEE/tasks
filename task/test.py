num_list = [1,0.4,2,3,"test",5,8,19,23,5,0.71, 2]
print(num_list)

for i in range(int(len(num_list) / 2)):
    num_list[i], num_list[len(num_list)-i-1] = num_list[len(num_list)-i-1], num_list[i]

print(num_list)
