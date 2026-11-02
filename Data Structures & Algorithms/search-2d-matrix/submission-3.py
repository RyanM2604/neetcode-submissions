class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        l, r = 0, ROWS * COLS - 1

        while l <= r:
            mid = (l + r) // 2

            row_select = mid // COLS
            col_select = mid % COLS

            if matrix[row_select][col_select] == target:
                return True
            elif matrix[row_select][col_select] < target:
                l = mid + 1
            else:
                r = mid - 1
        
        return False
