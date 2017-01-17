class Solution(object):
    def moveZeroes(self, nums):
        length = len(nums)
        lastIndex = 0
        for p1 in range(0, length):
            if nums[p1] != 0:
                nums[lastIndex] = nums[p1]
                lastIndex = lastIndex + 1
        while lastIndex < length:
            nums[lastIndex] = 0
            lastIndex = lastIndex + 1
        return nums

    def moveZeroes1(self, nums):
        i = j = 0
        while i < len(nums):
            if nums[i] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
            i += 1
        return nums


nums1 = [0, 1, 0, 3, 12]  # [1, 3, 12, 0, 0]
print(Solution().moveZeroes(nums1))
print(Solution().moveZeroes1(nums1))
