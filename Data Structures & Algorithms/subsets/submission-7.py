class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []

        def backtrack(i, sol):
            if i == n:
                res.append(sol[:])
                return
            
            sol.append(nums[i])
            backtrack(i + 1, sol)
            sol.pop()

            backtrack(i + 1, sol)
        
        backtrack(0, [])
        return res