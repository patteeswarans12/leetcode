class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p)>len(s):
            return []
        l=[0]*26
        k=len(p)
        for i in range(k):
            l[ord(p[i])-97]+=1
        m=[0]*26
        for i in range(k):
            m[ord(s[i])-97]+=1
        r=[]
        if l==m:
            r.append(0)
        for i in range(1,len(s)-k+1):
            c=ord(s[i-1])-97
            m[c]-=1
            ch=ord(s[i+k-1])-97
            m[ch]+=1
            if l==m:
                r.append(i)
        return r