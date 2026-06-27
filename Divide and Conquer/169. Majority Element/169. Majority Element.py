class Solution(object):
    def majorityElement(self, nums):
        d = {}
        for i in nums:
            d[i] = d.get(i, 0) + 1
        return max(d, key=d.get)