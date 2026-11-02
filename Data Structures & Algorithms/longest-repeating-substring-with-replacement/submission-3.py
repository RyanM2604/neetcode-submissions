class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        lookup = {}
        maxF = 0
        res = 0

        l = 0

        for r in range(len(s)):
            lookup[s[r]] = lookup.get(s[r], 0) + 1
            maxF = max(maxF, lookup[s[r]])

            # You need maxF as through that you can know the other chars are the ones to be replaced
            while (r - l + 1) - maxF > k:
                lookup[s[l]] -= 1
                l += 1
            
            res = max(res, (r - l + 1))
        
        return res