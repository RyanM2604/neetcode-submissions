class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        myDict = {}

        for num in nums:
            myDict[num] = myDict.get(num, 0) + 1
        
        heap = []
        for num in myDict.keys():
            heapq.heappush(heap, (myDict[num], num))
            if len(heap) > k:
                heapq.heappop(heap)
        
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        
        return res