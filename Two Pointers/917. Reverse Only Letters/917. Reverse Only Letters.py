class Solution(object):
    def reverseOnlyLetters(self, s):
        i=0
        j=len(s)-1
        sl=list(s)
        while i<j:
            if not sl[i].isalpha() :
                i+=1
            elif not sl[j].isalpha():
                j-=1
            else:
                sl[i],sl[j]=sl[j],sl[i]
                i+=1
                j-=1
        return ''.join(sl)