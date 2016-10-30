s = "sabrrtuwacaddabra"

final = ''
cur = ''
prev = ''

for i in s:
    if i >= prev:
        cur += i
        if len(final) < len(cur):
            final = cur
    else:
        cur = i
    prev = i

print(final)
