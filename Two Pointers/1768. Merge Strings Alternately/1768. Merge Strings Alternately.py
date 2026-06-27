class Solution:
    def mergeAlternately(self, w1: str, w2: str):
        i=0
        s=''
        while i<len(w1) or i<len(w2):
            if i<len(w1):
                s+=w1[i]
            if i<len(w2):
                s+=w2[i]
            i+=1
        
        return s
