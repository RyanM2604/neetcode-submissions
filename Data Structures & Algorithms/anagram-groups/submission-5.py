class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        lookup = defaultdict(list)

        for s in strs:
            hash_ = [0] * 26
            for c in s:
                hash_[ord(c) - ord('a')] += 1
            
            lookup[tuple(hash_)].append(s)
        
        return list(lookup.values())
