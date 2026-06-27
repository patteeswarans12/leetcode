class Solution(object):
    def reverseVowels(self, s):
        v=set('aeiouAEIOU')
        i=0
        j=len(s)-1
        l=[m  for m in s]
        while i<j:
            while i<j and l[i] not in  v:
                i+=1
            while i<j and l[j] not in v:
                j-=1
            l[i],l[j]=l[j],l[i]
            i+=1
            j-=1
        return ''.join(l)