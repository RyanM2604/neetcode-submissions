class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        lookup = {}
        res = 0

        l = 0
        maxF = 0
        for r in range(len(s)):
            lookup[s[r]] = 1 + lookup.get(s[r], 0)
            maxF = max(maxF, lookup[s[r]])

            while (r - l + 1) - maxF > k:
                lookup[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        
        return res