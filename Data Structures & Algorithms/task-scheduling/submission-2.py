class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        lookup = {}
        
        for task in tasks:
            lookup[task] = lookup.get(task, 0) + 1
        
        maxHeap = []

        for cnt in lookup.values():
            maxHeap.append(-cnt)
        
        heapq.heapify(maxHeap)

        q = deque()
        time = 0

        while q or maxHeap:
            time += 1

            if maxHeap:
                process = 1 + heapq.heappop(maxHeap)
                if process:
                    q.append((process, time + n))
            
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        
        return time