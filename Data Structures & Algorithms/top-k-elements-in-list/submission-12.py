class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        lookup = {}
        res = []

        for num in nums:
            lookup[num] = lookup.get(num, 0) + 1
        
        heap = []

        for num, freq in lookup.items():
            heapq.heappush(heap, (-freq, num))
        
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        
        return res