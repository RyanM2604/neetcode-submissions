class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(i, sol):
            #base case
            if len(nums) == i:
                res.append(sol[:])
                return
            
            #choose num
            sol.append(nums[i])
            backtrack(i + 1, sol)
            sol.pop()

            #dont choose num
            backtrack(i + 1, sol)
        
        backtrack(0, [])
        return res

            
