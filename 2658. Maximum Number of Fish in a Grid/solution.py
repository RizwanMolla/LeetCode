class Solution:
    def findMaxFish(self, grid: list[list[int]]) -> int:

        m, n = len(grid), len(grid[0])

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        def dfs(r, c):
            if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] == 0:
                return 0
            
            fish = grid[r][c]
            grid[r][c] = 0
            
            for dr, dc in directions:
                fish += dfs(r + dr, c + dc)
            
            return fish
        
        max_fish = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0:
                    max_fish = max(max_fish, dfs(i, j))
        
        return max_fish
