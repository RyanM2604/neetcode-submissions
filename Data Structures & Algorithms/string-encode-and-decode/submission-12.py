class Solution:

    def encode(self, strs: List[str]) -> str:
        # 5#hello
        res = ""

        for s in strs:
            length = str(len(s))
            res += (length + '#' + s)
        
        return res

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []

        while i < len(s):
            j = i

            while s[j] != '#':
                j += 1
            
            length = int(s[i:j])

            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j
        
        return res

            
