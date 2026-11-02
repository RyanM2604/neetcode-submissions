class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for string in strs:
            key = 26 * [0]
            for char in string:
                key[ord('a') - ord(char)] += 1
            
            res[tuple(key)].append(string)
        
        return list(res.values())