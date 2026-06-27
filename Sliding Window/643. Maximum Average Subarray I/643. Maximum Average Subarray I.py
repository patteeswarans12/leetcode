class Solution:
    def findMaxAverage(self, n: List[int], k: int) -> float:
        c=0
        for i in range(k):
            c+=n[i]
        m=c/k
        r=0
        for i in range(1,len(n)-k+1):
            c+=-n[i-1]+n[i+k-1]
            r=c/k
            m=max(r,m)

        return m