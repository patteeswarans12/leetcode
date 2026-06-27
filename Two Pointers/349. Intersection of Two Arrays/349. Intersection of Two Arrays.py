class Solution(object):
    def intersection(self, n1, n2):
        
        l=list(set(n1) & set(n2))
        return l        