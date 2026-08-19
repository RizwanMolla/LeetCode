from collections import defaultdict
from typing import List

class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        diagonals = defaultdict(list)

        # Step 1: Collect diagonals
        for i in range(n):
            for j in range(n):
                diagonals[i - j].append(grid[i][j])

        # Step 2: Sort according to rule
        for key in diagonals:
            if key >= 0:  # bottom-left
                diagonals[key].sort(reverse=True)  # non-increasing
            else:  # top-right
                diagonals[key].sort()  # non-decreasing

        # Step 3: Put back values
        for i in range(n):
            for j in range(n):
                grid[i][j] = diagonals[i - j].pop(0)

        return grid
