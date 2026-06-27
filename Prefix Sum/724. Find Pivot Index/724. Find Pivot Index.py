class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        t=sum(nums)
        l=0
        for i in range(len(nums)):
            if l==t-l-nums[i]:
                return i
            l+=nums[i]
        return -1