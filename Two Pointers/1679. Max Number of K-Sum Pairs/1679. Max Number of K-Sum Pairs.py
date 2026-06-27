class Solution:
    def maxOperations(self, n: List[int], k: int) -> int:
        c=0
        l=0
        r=len(n)-1
        n.sort()
        while l<r:
            s= n[l]+n[r]
              
            if s==k:
                c+=1
                l+=1
                r-=1
            elif s<k:
                l+=1
            else:
                r-=1
        return c