class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i in range(len(nums)):
            j, k = i + 1, len(nums) - 1

            while j < k:
                total = nums[j] + nums[k] + nums[i]
                if total == 0:
                    if [nums[i], nums[j], nums[k]] not in res:
                        res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                if total < 0:
                    j += 1
                if total > 0:
                    k -= 1
        
        return res