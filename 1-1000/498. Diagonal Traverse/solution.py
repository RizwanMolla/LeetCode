class Solution:
    def findDiagonalOrder(self, mat: list[list[int]]) -> list[int]:
        if not mat or not mat[0]:
            return []

        m, n = len(mat), len(mat[0])
        result = []
        row, col = 0, 0
        up_right_dir = True

        while len(result) < m * n:
            result.append(mat[row][col])

            if up_right_dir:
                new_row, new_col = row - 1, col + 1
                if new_row < 0 or new_col >= n:
                    up_right_dir = False
                    if new_col >= n:
                        row += 1
                    else:
                        col += 1
                else:
                    row, col = new_row, new_col
            else:  # down-left
                new_row, new_col = row + 1, col - 1
                if new_row >= m or new_col < 0:
                    up_right_dir = True
                    if new_row >= m:
                        col += 1
                    else:
                        row += 1
                else:
                    row, col = new_row, new_col
        
        return result