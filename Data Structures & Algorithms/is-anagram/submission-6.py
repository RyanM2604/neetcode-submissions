class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        slookup = [0] * 26
        tlookup = [0] * 26

        for i in range(len(s)):
            slookup[ord(s[i]) - ord('a')] += 1
            tlookup[ord(t[i]) - ord('a')] += 1
        
        return slookup == tlookup