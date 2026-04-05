class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])

        lo, hi = 0, m*n - 1

        while lo <= hi:
            mid = (lo + hi)//2
            row = mid//n
            col = mid%n

            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                lo = mid + 1
            else:
                hi = mid - 1

        return False      