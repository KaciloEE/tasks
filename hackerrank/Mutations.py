str = input().strip()
str1 = input().split()
n = int(str1[0])
n2 = str1[1]
str = str[:n] + n2 + str[n + 1:]
print(str)
