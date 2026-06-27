class Solution(object):
    def maximumWealth(self, a):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        m=0
        for i in a:
            m=max(m,sum(i))
        return m