class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        lookup = set(nums)
        res = 0

        for num in nums:
            if num - 1 not in lookup:
                length = 1
                while num + length in lookup:
                    length += 1
                res = max(res, length)
        
        return res