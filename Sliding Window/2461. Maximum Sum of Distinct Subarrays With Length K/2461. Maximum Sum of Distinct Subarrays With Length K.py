class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        d = {}
        curr_sum = 0
        ans = 0

        for i in range(len(nums)):
            curr_sum += nums[i]
            d[nums[i]] = d.get(nums[i], 0) + 1

            if i >= k:
                curr_sum -= nums[i - k]
                d[nums[i - k]] -= 1
                if d[nums[i - k]] == 0:
                    del d[nums[i - k]]

            if i >= k - 1 and len(d) == k:
                ans = max(ans, curr_sum)

        return ans