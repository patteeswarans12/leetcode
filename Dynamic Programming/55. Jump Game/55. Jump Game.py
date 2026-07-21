class Solution:
    def canJump(self, nums: List[int]) -> bool:
        s = 0

        for i in range(len(nums)):
            if i > s:
                return False

            s = max(s, i + nums[i])

        return True