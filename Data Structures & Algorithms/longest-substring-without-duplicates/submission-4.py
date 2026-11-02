class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        longest = 0

        seen = set()

        while r < len(s):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            
            seen.add(s[r])

            length = r - l + 1
            longest = max(length, longest)

            r += 1
        
        return longest
