class Solution(object):
    def findDisappearedNumbers(self, nums):
         return list(set(range(1, len(nums)+1)) - set(nums))


n = [1,1]
print(Solution().findDisappearedNumbers(n))

'''
Input: [4,3,2,7,8,2,3,1]
Output:[5,6]

Input: [1,1]
Output:[2]
'''
