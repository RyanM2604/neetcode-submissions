class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        fingerprintS1 = [0] * 26
        fingerprintS2 = [0] * 26

        l, r = 0, 0
        
        for r in range(len(s1)):
            fingerprintS1[ord(s1[r]) - ord('a')] += 1
            fingerprintS2[ord(s2[r]) - ord('a')] += 1
        
        while r < len(s2) - 1:
            if fingerprintS1 == fingerprintS2:
                return True
            
            fingerprintS2[ord(s2[l]) - ord('a')] -= 1
            l += 1
            r += 1
            fingerprintS2[ord(s2[r]) - ord('a')] += 1
        
        return fingerprintS1 == fingerprintS2