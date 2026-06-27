class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        d = {}

        for ch in s:
            d[ch] = d.get(ch, 0) + 1

        for ch in t:
            if ch not in d or d[ch] == 0:
                return ch
            d[ch] -= 1