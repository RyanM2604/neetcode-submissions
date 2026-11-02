class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        low, high = 0, (ROWS * COLS) - 1

        while low <= high:
            mid = (low + high) // 2
            mid_row = mid // COLS
            mid_col = mid % COLS

            if matrix[mid_row][mid_col] == target:
                return True
            elif matrix[mid_row][mid_col] < target:
                low = mid + 1
            else:
                high = mid - 1
            
        return False