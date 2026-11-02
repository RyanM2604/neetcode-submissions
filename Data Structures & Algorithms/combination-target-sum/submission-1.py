class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(i, sol, total):
            if total == target:
                res.append(sol[:])
            if i == len(nums):
                res.append(sol[:])
                return
            
            for idx in range(i, len(nums)):
                if total + nums[idx] > target:
                    continue
                
                sol.append(nums[idx])
                backtrack(idx, sol, total + nums[idx])
                sol.pop()
        
        backtrack(0, [], 0)

        return res



