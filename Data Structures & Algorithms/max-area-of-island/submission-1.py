class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        maxArea = 0
        visited = set()
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def dfs(r, c, length):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or (r, c) in visited or grid[r][c] == 0:
                return 0
            
            visited.add((r, c))
            length = 1

            for dx, dy in directions:
                length += dfs(r + dx, c + dy, length)
            
            return length


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r, c) not in visited:
                    maxArea = max(maxArea, dfs(r, c, 0))
        
        return maxArea

