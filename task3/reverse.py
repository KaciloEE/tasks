s = "яблоки вкусные"

s = s[::-1].split(' ')

print(" ".join(sorted(s, reverse=True)))
