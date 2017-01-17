a = 'ambulance'
print(a[::-1])


def reverse_a_string_more_slowly(a_string):
    new_strings = []
    index = len(a_string)
    while index:
        index -= 1
        new_strings.append(a_string[index])
    return ''.join(new_strings)

print(reverse_a_string_more_slowly(
    ['a', 'm', 'b', 'u', 'l', 'a', 'n', 'c', 'e']))


def rev(s):
    l = 0
    r = len(s) - 1
    while (l <= r):
        s[l], s[r] = s[r], s[l]
        l += 1
        r -= 1
    return "".join(s)


print(rev(['a', 'm', 'b', 'u', 'l', 'a', 'n', 'c', 'e']))
