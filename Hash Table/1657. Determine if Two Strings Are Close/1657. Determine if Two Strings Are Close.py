class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        
        # Frequency counts
        freq1 = [0] * 26
        freq2 = [0] * 26
        
        for c in word1:
            freq1[ord(c) - ord('a')] += 1
        for c in word2:
            freq2[ord(c) - ord('a')] += 1
        
        # Check same characters (both present or both absent)
        for i in range(26):
            if (freq1[i] > 0) != (freq2[i] > 0):
                return False
        
        # Check sorted frequencies match
        sorted_freq1 = sorted(freq1)
        sorted_freq2 = sorted(freq2)
        
        return sorted_freq1 == sorted_freq2