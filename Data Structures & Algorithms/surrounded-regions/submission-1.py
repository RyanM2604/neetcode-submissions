class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        visited = set()
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def dfs(r, c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or (r, c) in visited or board[r][c] == 'X':
                return 
            
            visited.add((r, c))
            board[r][c] = '#'

            for dx, dy in directions:
                dfs(r + dx, c + dy)

        
        for c in range(COLS):
            if board[0][c] == 'O':
                dfs(0, c)
        
        for r in range(ROWS):
            if board[r][0] == 'O':
                dfs(r, 0)
        
        for c in range(COLS):
            if board[ROWS - 1][c] == 'O':
                dfs(ROWS - 1, c)
            
        for r in range(ROWS):
            if board[r][COLS - 1] == 'O':
                dfs(r, COLS - 1)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                
                if board[r][c] == '#':
                    board[r][c] = 'O'
        

                    