class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)

        def backtrack(i, sol):
            if i == n:
                res.append(sol[:])
                return
            
            backtrack(i + 1, sol)

            sol.append(nums[i])
            backtrack(i + 1, sol)
            sol.pop()
        
        backtrack(0, [])
        return res