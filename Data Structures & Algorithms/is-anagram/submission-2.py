class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False
        
        counts = [0] * 26
        countt = [0] * 26

        for c in range(len(s)):
            counts[ord(s[c]) - ord('a')] += 1
            countt[ord(t[c]) - ord('a')] += 1
        
        return counts == countt