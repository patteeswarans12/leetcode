class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n=len(code)
        l=[0]*n
        if k==0:
            return l
        
        for i in range(n):
            s=0

            y=i+1
            if k<0:
                y=i-1
                while y>i+k-1 and k<0:
                    s+=code[y%n]
                    y-=1
            while y<i+k+1 and k>0:
                s+=code[y%n]
                y+=1
            l[i]=s
        return l