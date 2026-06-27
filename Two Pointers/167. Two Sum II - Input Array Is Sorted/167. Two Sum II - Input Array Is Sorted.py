class Solution(object):
    def twoSum(self, n, t):
        i=0
        j=len(n)-1
        while i<j:
            s=n[i]+n[j]
            if s==t:
                return [i+1,j+1]
            elif s>t:
                j-=1
            else:
                i+=1
        