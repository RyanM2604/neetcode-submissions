class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res, part = [], []
        n = len(s)

        def backtrack(i):
            if i >= n:
                res.append(part[:])
                return
            
            for j in range(i, n):
                if self.palindrome(s, i, j):
                    part.append(s[i : j + 1])
                    backtrack(j + 1)
                    part.pop()
        
        backtrack(0)
        return res


    def palindrome(self, s, l, r):

        while l < r:
            if s[l] != s[r]:
                return False

            l += 1
            r -= 1
        
        return True