class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        l = 0
        r = m * n

        while r - l > 1:
            mid = l + (r - l) // 2
            row = mid // n
            col = mid % n
            value = matrix[row][col]

            if value <= target:
                l = mid
            else:
                r = mid

        return matrix[l // n][l % n] == target