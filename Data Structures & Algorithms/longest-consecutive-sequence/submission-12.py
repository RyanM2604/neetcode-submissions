class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        seen = set(nums)
        longest = 0

        for num in seen:

            # start of sequence
            if num - 1 not in seen:

                length = 1

                while num + length in seen:
                    length += 1

                longest = max(longest, length)

        return longest