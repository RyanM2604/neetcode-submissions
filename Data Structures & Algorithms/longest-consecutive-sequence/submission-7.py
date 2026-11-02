class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        lookup = set(nums)
        maxLength = 0

        for num in lookup:
            if (num - 1) not in lookup:
                length = 1
                while (num + length) in lookup:
                    length += 1
                maxLength = max(length, maxLength)
            
        return maxLength