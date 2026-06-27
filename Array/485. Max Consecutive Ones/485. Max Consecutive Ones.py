class Solution(object):
    def findMaxConsecutiveOnes(self, n):
        """
        :type nums: List[int]
        :rtype: int
        """
        c=0
        m=0

        for i in n:
            if i==1:
                c+=1
                m=max(c,m)
            else:
                c=0
        return m