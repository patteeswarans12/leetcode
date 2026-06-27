class Solution(object):
    def removeElement(self, nums, val):
        c=nums.count(val)
        for i in range(c):
            nums.remove(val)