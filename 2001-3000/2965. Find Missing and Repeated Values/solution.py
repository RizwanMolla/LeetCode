from typing import List

class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        num_count = {}
        
        for row in grid:
            for num in row:
                num_count[num] = num_count.get(num, 0) + 1
        
        repeated, missing = -1, -1
        for i in range(1, n * n + 1):
            if i in num_count:
                if num_count[i] == 2:
                    repeated = i
            else:
                missing = i
        
        return [repeated, missing]
