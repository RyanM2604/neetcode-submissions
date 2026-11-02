class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False
        
        countS = {}
        countT = {}

        for i in range(len(s)):
            countS[ord(s[i]) - ord('a')] = countS.get(ord(s[i]) - ord('a'), 0) + 1
            countT[ord(t[i]) - ord('a')] = countT.get(ord(t[i]) - ord('a'), 0) + 1
        
        return countS == countT
