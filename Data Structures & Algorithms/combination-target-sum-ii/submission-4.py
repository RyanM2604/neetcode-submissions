class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        n = len(candidates)
        res = []

        def backtrack(i, sol, total):
            if total == target:
                res.append(sol[:])
                return
            
            if total > target:
                return
            
            for j in range(i, n):
                if j > i and candidates[j] == candidates[j - 1]:
                    continue
                
                sol.append(candidates[j])
                backtrack(j + 1, sol, total + candidates[j])
                sol.pop()
        
        backtrack(0, [], 0)
        return res