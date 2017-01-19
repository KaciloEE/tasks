# s = "anagram" t = "nagaram" return true.
# s = "rat", t = "car", return false.


class Solution(object):
    def isAnagram(self, s, t):
        return True if sorted(s) == sorted(t) else False


print(Solution().isAnagram("anagram", "nagaram"))

# def isAnagram1(self, s, t):
#     dic1, dic2 = {}, {}
#     for item in s:
#         dic1[item] = dic1.get(item, 0) + 1
#     for item in t:
#         dic2[item] = dic2.get(item, 0) + 1
#     return dic1 == dic2
