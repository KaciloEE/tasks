def findComplement(num):
    i = 1
    while i <= num:
        print(i)
        i = i << 1
        #print(i)
    return (i - 1) ^ num

print(findComplement(5))