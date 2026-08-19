from typing import List

class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        
        top_prefix = [0] * n
        bottom_prefix = [0] * n

        top_prefix[0] = grid[0][0]
        for i in range(1, n):
            top_prefix[i] = top_prefix[i - 1] + grid[0][i]

        bottom_prefix[0] = grid[1][0]
        for i in range(1, n):
            bottom_prefix[i] = bottom_prefix[i - 1] + grid[1][i]
        min_second_robot_points = float('inf')

        for i in range(n):
            points_above = top_prefix[n - 1] - top_prefix[i]
            points_below = bottom_prefix[i - 1] if i > 0 else 0            
            second_robot_points = max(points_above, points_below)
            min_second_robot_points = min(min_second_robot_points, second_robot_points)

        return min_second_robot_points
