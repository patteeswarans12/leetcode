class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        c=0
        a=0
        for i in gain:
            c+=i
            a=max(a,c)
        return a