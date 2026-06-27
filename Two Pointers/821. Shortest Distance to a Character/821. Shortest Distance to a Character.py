class Solution(object):
    def shortestToChar(self, s, c):
        pos = []
        
        for i in range(len(s)):
            if s[i] == c:
                pos.append(i)

        ans = []

        for i in range(len(s)):
            m = float('inf')

            for j in pos:
                m = min(m, abs(i - j))

            ans.append(m)

        return ans