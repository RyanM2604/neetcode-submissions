class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)

        def backtrack(i, sol):
            res.append(sol[:])
            
            for j in range(i, n):
                sol.append(nums[j])
                backtrack(j + 1, sol)
                sol.pop()
        
        backtrack(0, [])
        return res
