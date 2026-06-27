class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        c=0
        v='aeiouAEIOU'
        for i in range(k):
            if s[i] in v:
                c+=1

        m=c
        for i in range(k,len(s)):
            if s[i-k] in v:
                c-=1
            if s[i] in v:
                c+=1
            m=max(c,m)
        return m