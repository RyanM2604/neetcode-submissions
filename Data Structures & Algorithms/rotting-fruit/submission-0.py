class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        q = deque()
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        totalFruit = 0

        def addNode(r, c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == 0 or (r, c) in visited:
                return
            
            visited.add((r, c))
            q.append((r, c))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    totalFruit += 1
                    q.append((r, c))
                    visited.add((r, c))

                if grid[r][c] == 1:
                    totalFruit += 1
        
        time = 0
        while q and len(visited) < totalFruit:
            for i in range(len(q)):
                r, c = q.popleft()

                for dx, dy in directions:
                    addNode(r + dx, c + dy)
            
            time += 1
        
        return time if len(visited) == totalFruit else -1

            


