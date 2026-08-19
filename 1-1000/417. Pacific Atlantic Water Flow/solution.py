class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []

        m, n = len(heights), len(heights[0])
        pacific = set()
        atlantic = set()

        def dfs(r, c, visited, prev_height):
            # Out of bounds or already visited or lower height (cannot flow upward)
            if (r, c) in visited or r < 0 or c < 0 or r >= m or c >= n or heights[r][c] < prev_height:
                return
            visited.add((r, c))
            # Explore 4 directions
            dfs(r + 1, c, visited, heights[r][c])
            dfs(r - 1, c, visited, heights[r][c])
            dfs(r, c + 1, visited, heights[r][c])
            dfs(r, c - 1, visited, heights[r][c])

        # Start DFS from Pacific Ocean edges (top row + left column)
        for c in range(n):
            dfs(0, c, pacific, heights[0][c])  # top row
            dfs(m - 1, c, atlantic, heights[m - 1][c])  # bottom row
        for r in range(m):
            dfs(r, 0, pacific, heights[r][0])  # left column
            dfs(r, n - 1, atlantic, heights[r][n - 1])  # right column

        # Intersection of cells that can reach both oceans
        res = list(pacific & atlantic)
        return res
