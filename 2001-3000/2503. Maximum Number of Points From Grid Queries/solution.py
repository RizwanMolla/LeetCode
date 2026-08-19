from heapq import heappop, heappush
from itertools import pairwise
from typing import List

class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        rows, cols = len(grid), len(grid[0])
        sorted_queries = sorted((val, idx) for idx, val in enumerate(queries))
        result = [0] * len(sorted_queries)
        min_heap = [(grid[0][0], 0, 0)]
        points_collected = 0
        visited = [[False] * cols for _ in range(rows)]
        visited[0][0] = True
        
        for threshold, index in sorted_queries:
            while min_heap and min_heap[0][0] < threshold:
                _, r, c = heappop(min_heap)
                points_collected += 1
                for dr, dc in pairwise((-1, 0, 1, 0, -1)):
                    new_r, new_c = r + dr, c + dc
                    if 0 <= new_r < rows and 0 <= new_c < cols and not visited[new_r][new_c]:
                        heappush(min_heap, (grid[new_r][new_c], new_r, new_c))
                        visited[new_r][new_c] = True
            result[index] = points_collected
        
        return result