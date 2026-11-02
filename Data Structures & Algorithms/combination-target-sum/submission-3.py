class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(nums)

        def backtrack(i, sol, total):

            if total == target:
                res.append(sol[:])
                return
            

            for j in range(i, n):
                if total > target:
                    continue
                
                sol.append(nums[j])
                backtrack(j, sol, total + nums[j])
                sol.pop()
            
        backtrack(0, [], 0)
        return res