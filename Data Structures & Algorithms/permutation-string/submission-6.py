class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        countS1 = [0] * 26
        countS2 = [0] * 26
        
        l, r = 0, 0

        while r < len(s1):
            countS1[ord(s1[r]) - ord('a')] += 1
            countS2[ord(s2[r]) - ord('a')] += 1
            r += 1
        
        while r < len(s2):
            if countS1 == countS2:
                return True

            countS2[ord(s2[r]) - ord('a')] += 1
            countS2[ord(s2[l]) - ord('a')] -= 1

            r += 1
            l += 1
        
        return countS1 == countS2