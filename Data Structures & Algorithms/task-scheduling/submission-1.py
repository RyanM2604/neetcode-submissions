class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        lookup = {}
        maxHeap = []
        
        for task in tasks:
            if task not in lookup:
                lookup[task] = 0
            lookup[task] += 1
        
        for value in lookup.values():
            maxHeap.append(-value)
        
        heapq.heapify(maxHeap)

        time = 0
        q = deque()

        while maxHeap or q:
            time += 1
            
            if maxHeap:
                process = 1 + heapq.heappop(maxHeap)
                if process:
                    q.append((process, time + n))

            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        
        return time
            