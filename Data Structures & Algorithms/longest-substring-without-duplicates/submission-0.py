class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        strlen = l = 0
        lookup = set()

        for r in range(len(s)):
            while s[r] in lookup: # while is needed if multiple duplicates in a row
                lookup.remove(s[l])
                l += 1
            lookup.add(s[r])
            strlen = max(strlen, r - l + 1)
        
        return strlen