def rev(s):
    l = []
    index = len(s)
    while index:
        index -= 1
        l.append(s[index])
    return "".join(l)

print(rev('ambul'))
