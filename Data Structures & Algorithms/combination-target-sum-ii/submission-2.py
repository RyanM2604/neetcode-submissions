class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        n = len(candidates)

        def backtrack(i, sol, total):
            if total == target:
                res.append(sol[:])
                return
            
            

            for j in range(i, n):
                if j > i and candidates[j - 1] == candidates[j]:
                    continue
                
                if total > target:
                    continue
                
                sol.append(candidates[j])
                backtrack(j + 1, sol, total + candidates[j])
                sol.pop()
        
        backtrack(0, [], 0)
        return res