class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        check_s1 = [0] * 26
        check_s2 = [0] * 26

        for i in range(len(s1)):
            check_s1[ord(s1[i]) - ord('a')] += 1
            check_s2[ord(s2[i]) - ord('a')] += 1
        
        l, r = 0, len(s1)

        while r < len(s2):
            if check_s1 == check_s2:
                return True
            
            check_s2[ord(s2[l]) - ord('a')] -= 1
            check_s2[ord(s2[r]) - ord('a')] += 1
            l += 1
            r += 1

        return check_s1 == check_s2
        