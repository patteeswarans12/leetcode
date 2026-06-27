class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        r=''
        m=0
        i=0
    
        while i<len(s):
            if s[i] not in r:
                r+=s[i]
                i+=1
            else:
                m=max(m,len(r))
                c=r.index(s[i])
            
                r=r[c+1:]+s[i]
                i+=1
        m=max(m,len(r))
        return m