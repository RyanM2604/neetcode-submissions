class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []

        def backtrack(i, sol):
            res.append(sol[:])
            
            for j in range(i, n):
                if j > i and nums[j - 1] == nums[j]:
                    continue
                
                sol.append(nums[j])
                backtrack(j + 1, sol)
                sol.pop()
        
        backtrack(0, [])
        return res