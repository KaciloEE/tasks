#Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. Since 2 has only one digit, return it.
class Solution(object):
    def addDigits(self, num):
        x = num
        n = num
        n1 = 0
        while n > 1:
            s = list(map(int,str(x)))
            if len(s) != 1:
                x = sum(s)
            else:
                n1 = s[0]

            n = len(s)
        return num if num == 1 else n1


print(Solution().addDigits(38))

def addDigits(num):
    return num % 9 or num and 9

print(addDigits(38))
