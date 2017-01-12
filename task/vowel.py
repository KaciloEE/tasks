s = 'programming'
s1 =[]

for item in s:
  if item in 'aeiou':
    s1.append(item)

print("".join(s1))
