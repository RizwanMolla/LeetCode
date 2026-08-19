from collections import deque

class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        queue = deque([(0, 0, 0)])
        visited = [[False] * n for _ in range(m)]
        
        while queue:
            cost, x, y = queue.popleft()
            
            if x == m - 1 and y == n - 1:
                return cost
            
            if visited[x][y]:
                continue
            visited[x][y] = True
            
            for i, (dx, dy) in enumerate(directions):
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                
                    if i + 1 == grid[x][y]:
                        queue.appendleft((cost, nx, ny))
                    else:
                        queue.append((cost + 1, nx, ny))
                        
        return -1
