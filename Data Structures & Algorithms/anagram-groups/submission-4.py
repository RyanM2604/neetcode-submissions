class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        lookup = defaultdict(list)

        for s in strs:
            signature = [0] * 26
            for c in s:
                signature[ord(c) - ord('a')] += 1
            
            signature = tuple(signature)
            lookup[signature].append(s)

        return list(lookup.values())