class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += (str(len(s)) + '#' + s)
        
        return res

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []

        while i < len(s) - 1:
            j = i
            while s[j] != '#':
                j += 1
            
            length = s[i:j]
            j += 1
            i = j + int(length)
            res.append(s[j:i])
        
        return res