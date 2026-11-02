class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low = 0
        high = len(matrix) * len(matrix[0]) - 1
        cols = len(matrix[0])

        while low <= high:
            mid = (high + low) // 2

            if matrix[mid// cols][mid % cols] == target:
                return True
            elif matrix[mid// cols][mid % cols] > target:
                high = mid - 1
            else:
                low = mid + 1
        return False