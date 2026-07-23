class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])

        # Check if first row has any zero
        first_row = False
        for j in range(n):
            if matrix[0][j] == 0:
                first_row = True
                break

        # Check if first column has any zero
        first_col = False
        for i in range(m):
            if matrix[i][0] == 0:
                first_col = True
                break

        # Use first row and first column as markers
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # Set cells to zero based on markers
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # Zero out first row if needed
        if first_row:
            for j in range(n):
                matrix[0][j] = 0

        # Zero out first column if needed
        if first_col:
            for i in range(m):
                matrix[i][0] = 0