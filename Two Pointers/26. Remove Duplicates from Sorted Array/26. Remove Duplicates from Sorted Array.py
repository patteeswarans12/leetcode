class Solution(object):
    def removeDuplicates(self, nums):
        s = sorted(set(nums))

        for i in range(len(s)):
            nums[i] = s[i]

        return len(s)