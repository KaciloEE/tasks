class Solution(object):
    def hammingDistance(self, x, y):
        return bin(x^y).count('1')

print(Solution().hammingDistance(1,4))