class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-x for x in stones]
        heapq.heapify(maxHeap)
        res = 0

        while len(maxHeap) > 1:
            stone_1 = -(heapq.heappop(maxHeap))
            stone_2 = -(heapq.heappop(maxHeap))

            if stone_1 == stone_2:
                continue
            else:
                heapq.heappush(maxHeap, -(abs(stone_1 - stone_2)))
        
        res = -(maxHeap[0] if maxHeap else 0)
        return res
