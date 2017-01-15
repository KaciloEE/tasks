class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        s_count = 0
        count = 0
        for i in nums:
            if i == 1:
                count += 1
                s_count = max(count,s_count)
            else:
                count = 0
        return s_count


print(Solution().findMaxConsecutiveOnes([1,1,0,1,1,1,0,1]))
