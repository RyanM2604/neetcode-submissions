class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        lookup = {}
        maxf = 0
        l = 0
        res = 0

        for r in range(len(s)):
            lookup[s[r]] = lookup.get(s[r], 0) + 1
            maxf = max(lookup[s[r]], maxf)
            
            while (r - l + 1) - maxf > k:
                lookup[s[l]] -= 1
                l += 1
            
            res = max(res, r - l + 1)
        
        return res