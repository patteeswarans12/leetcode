from typing import List

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        prev_ones = 0
        curr_ones = 0
        max_length = 0
        
        for num in nums:
            if num == 1:
                curr_ones += 1
            else:
                max_length = max(max_length, prev_ones + curr_ones)
                prev_ones = curr_ones
                curr_ones = 0
        
        max_length = max(max_length, prev_ones + curr_ones)
        
        if max_length == len(nums):
            return max_length - 1
        
        return max_length