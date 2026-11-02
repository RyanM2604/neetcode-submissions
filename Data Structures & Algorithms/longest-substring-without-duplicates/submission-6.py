class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lookup = set()
        longest = 0

        l, r = 0, 0

        while r < len(s):
            while s[r] in lookup:
                lookup.remove(s[l])
                l += 1
            
            lookup.add(s[r])
            length = r - l + 1
            longest = max(longest, length)

            r += 1
        
        return longest
            

