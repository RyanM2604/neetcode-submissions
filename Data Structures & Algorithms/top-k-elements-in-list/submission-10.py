class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        lookup = {}
        res = []

        for num in nums:
            lookup[num] = lookup.get(num, 0) + 1
        
        heap = []

        for key in lookup.keys():
            heapq.heappush(heap, [lookup[key], key])

            if len(heap) > k:
                heapq.heappop(heap)

        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        
        return res