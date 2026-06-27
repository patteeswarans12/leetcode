class Solution:
    def plusOne(self, d: List[int]) -> List[int]:
        s=''.join(map(str,d))
        m=int(s)+1
        d=[int(i) for i in str(m)]
        return d