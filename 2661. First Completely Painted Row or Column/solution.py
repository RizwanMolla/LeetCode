from typing import List

class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        position = {mat[i][j]: (i, j) for i in range(m) for j in range(n)}
        row_count = [0] * m
        col_count = [0] * n
        for i, num in enumerate(arr):
            r, c = position[num]
            row_count[r] += 1
            col_count[c] += 1
            if row_count[r] == n or col_count[c] == m:
                return i
        return -1

"""
Overview:
The solution first maps the values in the matrix to their respective row and column indices. As the elements in arr are processed, the corresponding row and column counters are incremented. When either a row or column reaches its full count, the index is returned. The approach runs in O(m * n) time and O(m + n) space.
"""