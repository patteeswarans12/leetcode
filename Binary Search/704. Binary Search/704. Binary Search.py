class Solution(object):
    def search(self, n, t):
        l=0
        r=len(n)-1
        while l<=r:
            m=(l+r)//2
            if n[m]==t:
                return m
            elif n[m]<t:
                l=m+1
            else:
                r=m-1
        return -1