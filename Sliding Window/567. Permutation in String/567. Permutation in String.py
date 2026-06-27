class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        else:
            k=len(s1)
            l=[0]*26
            for i in range(k):
                idx=ord(s1[i])-97
                l[idx]+=1
            m=[0]*26
            for i in range(k):
                idx=ord(s2[i])-97
                m[idx]+=1
            if l==m:
                return True
            for i in range(1,len(s2)-k+1):
                c=ord(s2[i-1])-97
                m[c]-=1
                ch=ord(s2[i+k-1])-97
                m[ch]+=1
                if m==l:
                    return True
            return False