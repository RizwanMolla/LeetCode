class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # Get dimensions of the matrix
        m, n = len(matrix), len(matrix[0])
        
        # Use first row and first column as markers
        # Track if first row and first column originally contain zeros
        first_row_has_zero = False
        first_col_has_zero = False
        
        # Check if first row has any zeros
        for j in range(n):
            if matrix[0][j] == 0:
                first_row_has_zero = True
                break
        
        # Check if first column has any zeros
        for i in range(m):
            if matrix[i][0] == 0:
                first_col_has_zero = True
                break
        
        # Use first row and first column to mark zeros
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0  # Mark the first cell in this row
                    matrix[0][j] = 0  # Mark the first cell in this column
        
        # Set zeros based on markers (except first row and column)
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        # Set first row to zeros if needed
        if first_row_has_zero:
            for j in range(n):
                matrix[0][j] = 0
        
        # Set first column to zeros if needed
        if first_col_has_zero:
            for i in range(m):
                matrix[i][0] = 0