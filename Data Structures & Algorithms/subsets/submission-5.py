class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)

        def backtrack(sol, i):
            if i == n:
                res.append(sol[:])
                return

            backtrack(sol, i + 1)

            sol.append(nums[i])
            backtrack(sol, i + 1)
            sol.pop()

            

        backtrack([], 0)
        return res