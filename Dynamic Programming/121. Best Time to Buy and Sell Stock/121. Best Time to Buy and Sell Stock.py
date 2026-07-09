class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m=float("inf")
        n=0
        for i in prices:
            m=min(m,i)
            n=max(n,i-m)
        return n