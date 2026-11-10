class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)

        def backtrack(sol):
            if len(sol) == n:
                res.append(sol[:])
                return 
            
            for j in range(n):
                if nums[j] in sol:
                    continue
                    
                sol.append(nums[j])
                backtrack(sol)
                sol.pop()
        
        backtrack([])

        return res