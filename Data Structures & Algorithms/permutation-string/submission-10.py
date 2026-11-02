class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        count_s1 = [0] * 26
        count_s2 = [0] * 26
        
        l, r = 0, 0

        for r in range(len(s1)):
            count_s1[ord(s1[r]) - ord('a')] += 1
            count_s2[ord(s2[r]) - ord('a')] += 1
        
        while r < len(s2) - 1:
            if count_s1 == count_s2:
                return True
            
            count_s2[ord(s2[l]) - ord('a')] -= 1

            l += 1
            r += 1

            count_s2[ord(s2[r]) - ord('a')] += 1
        

        return count_s1 == count_s2