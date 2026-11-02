class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        lookup = set(nums)

        for num in nums:
            if (num - 1) not in lookup:
                length = 1
                while (num + length) in lookup:
                    length += 1
                longest = max(length, longest)
        
        return longest