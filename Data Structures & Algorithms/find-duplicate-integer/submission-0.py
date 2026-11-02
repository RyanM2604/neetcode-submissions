class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        lookup = set()

        for num in nums:
            if num in lookup:
                return num
            
            lookup.add(num)