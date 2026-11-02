class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        lookup = {}
        res = []

        for num in nums:
            lookup[num] = lookup.get(num, 0) + 1
        
        heap = []

        for key, value in lookup.items():
            heapq.heappush(heap, (value, key))

            if len(heap) > k:
                heapq.heappop(heap)
        
        for value, key in heap:
            res.append(key)
        
        return res