class Solution(object):
    def thirdMax(self, n):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=list(set(n))
        n.sort()
        if len(n)<3:
            return n[-1]
        else:
            return n[-3]