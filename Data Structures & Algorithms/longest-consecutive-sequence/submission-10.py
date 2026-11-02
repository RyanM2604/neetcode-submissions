class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        longest = 0
        
        for i in range(len(nums)):
            curr = nums[i]
            cnt = 1
            
            while curr + 1 in seen:
                curr += 1
                cnt += 1
            
            longest = max(longest, cnt)

        return longest