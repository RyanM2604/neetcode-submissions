class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        lookup = {}
        
        for num in nums:
            lookup[num] = lookup.get(num, 0) + 1
        
        heap = []
        for num in lookup.keys():
            heapq.heappush(heap, (lookup[num], num))
            if len(heap) > k:
                heapq.heappop(heap)
        
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        
        return res