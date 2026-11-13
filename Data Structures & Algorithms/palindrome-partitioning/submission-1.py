class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        n = len(s)

        def isPalindrome(arr):
            l, r = 0, len(arr) - 1

            while l <= r:
                if arr[l] != arr[r]:
                    return False
                
                l += 1
                r -= 1
            
            return True

        def backtrack(sol, i):
            if i == n:
                res.append(sol[:])
                return
            
            for j in range(i, n):
                sub = s[i:j + 1]

                if not isPalindrome(sub):
                    continue
                
                sol.append(sub)
                backtrack(sol, j + 1)
                sol.pop()
        
        backtrack([], 0)
        return res
                


                