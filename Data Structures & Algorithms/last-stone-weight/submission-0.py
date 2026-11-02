class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxheap = [-s for s in stones] # converts to maxheap
        heapq.heapify(maxheap)

        while len(maxheap) > 1:
            x = -(heapq.heappop(maxheap))
            y = -(heapq.heappop(maxheap))

            if x < y:
                y -= x
                heapq.heappush(maxheap, -(y))
            elif y < x:
                x -= y
                heapq.heappush(maxheap, -(x))
        
        if maxheap:
            return -maxheap[0]
        else:
            return 0