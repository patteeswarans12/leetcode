class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        m=set(nums)
        i=1
        while i in m:
            i+=1
        return i