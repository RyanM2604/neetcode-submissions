class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        width = len(matrix[0])
        height = len(matrix)
        
        l = 0
        r = width * height - 1

        while l <= r:
            mid = l + (r - l) // 2

            if matrix[mid // width][mid % width] == target:
                return True
            elif matrix[mid // width][mid % width] < target:
                l = mid + 1
            else:
                r = mid - 1
        
        return False