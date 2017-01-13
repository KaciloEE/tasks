L = [x for x in range(1, 11)]
print(L)

left  = 0
right = len(L)-1

while (left < right):
    L[left], L[right] = L[right], L[left]
    left  += 1
    right -= 1


print(L)
