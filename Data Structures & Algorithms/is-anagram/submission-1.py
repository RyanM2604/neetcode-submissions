class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len (t):
            return False
        
        lookupS = {}
        lookupT = {}

        for i in range(len(s)):
            lookupS[s[i]] = 1 + lookupS.get(s[i], 0)
            lookupT[t[i]] = 1 + lookupT.get(t[i], 0)
        
        return lookupS == lookupT

        
        