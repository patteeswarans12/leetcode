class Solution(object):
    def maxArea(self, h):
        i=0
        j=len(h)-1
        m=0
        while i<j:
            w=j-i
            he=min(h[i],h[j])
            m=max(m,w*he)
            if h[i]<h[j]:
                i+=1
            else:
                j-=1
        return m