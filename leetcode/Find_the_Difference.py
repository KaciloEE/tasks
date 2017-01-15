class Solution(object):
    def findTheDifference(self, s, t):
        for ch in t:
            if (s+t).count(ch)%2:
                return ch;

print(Solution().findTheDifference("abcd","abcde"))
