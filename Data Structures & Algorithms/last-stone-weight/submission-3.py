class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-stone for stone in stones]

        heapq.heapify(heap)

        while len(heap) > 1:
            stone_1 = -(heapq.heappop(heap))
            stone_2 = -(heapq.heappop(heap))

            if stone_1 == stone_2:
                continue
            else:
                heapq.heappush(heap, -(abs(stone_1 - stone_2)))
        
        if heap:
            return -(heap[0])
        else:
            return 0