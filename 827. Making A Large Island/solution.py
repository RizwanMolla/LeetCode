class Solution:
    def largestIsland(self, grid: list[list[int]]) -> int:
        n = len(grid)
        island_id = 2
        island_sizes = {}
        
        def dfs(r, c, id):
            if r < 0 or r >= n or c < 0 or c >= n or grid[r][c] != 1:
                return 0
            grid[r][c] = id
            size = 1
            size += dfs(r + 1, c, id)
            size += dfs(r - 1, c, id)
            size += dfs(r, c + 1, id)
            size += dfs(r, c - 1, id)
            return size
        
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    size = dfs(i, j, island_id)
                    island_sizes[island_id] = size
                    island_id += 1
        
        max_size = max(island_sizes.values(), default=0)
        
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    neighbors = set()
                    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        r, c = i + dr, j + dc
                        if 0 <= r < n and 0 <= c < n and grid[r][c] != 0:
                            neighbors.add(grid[r][c])
                    new_size = 1
                    for neighbor_id in neighbors:
                        new_size += island_sizes.get(neighbor_id, 0)
                    max_size = max(max_size, new_size)
        
        return max_size