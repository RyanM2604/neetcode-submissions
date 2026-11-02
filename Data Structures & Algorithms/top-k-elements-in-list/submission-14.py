class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        res = []

        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        heap = []
        for key, freq in freq.items():
            heapq.heappush(heap, (freq, key))

            if len(heap) > k:
                heapq.heappop(heap)
        
        for i in range(k):
            res.append(heap[i][1])
        
        return res
