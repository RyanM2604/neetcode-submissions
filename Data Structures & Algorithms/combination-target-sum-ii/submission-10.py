class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(candidates)
        candidates.sort()

        def backtrack(sol, total, i):
            if total == target:
                res.append(sol[:])
                return
            
            if total > target:
                return
            
            for j in range(i, n):
                if j > i and candidates[j - 1] == candidates[j]:
                    continue
                
                sol.append(candidates[j])
                backtrack(sol, total + candidates[j], j + 1)
                sol.pop()
        
        backtrack([], 0, 0)
        return res
                
