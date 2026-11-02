class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxheap = []
        for x, y in points:
            dist = -(x*x + y*y)  # no sqrt needed
            heapq.heappush(maxheap, (dist, [x, y]))
            if len(maxheap) > k:
                heapq.heappop(maxheap)
        return [p for (_, p) in maxheap]