class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minheap = []
        res = []

        for point in points:
            minheap.append(((math.sqrt((point[0] - 0)**2 + (point[1] - 0)**2)), point))
        
        heapq.heapify(minheap)

        for i in range(k):
            res.append(heapq.heappop(minheap)[1])
        
        return res