class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        lookupS, lookupT = 26 * [0], 26 * [0]

        for i in range(len(s)):
            lookupS[ord('a') - ord(s[i])] += 1
            lookupT[ord('a') - ord(t[i])] += 1
        
        return lookupS == lookupT