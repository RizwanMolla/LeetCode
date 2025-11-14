class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        # Step 1: Create a (n+1)x(n+1) diff matrix
        diff = [[0] * (n + 1) for _ in range(n + 1)]

        # Step 2: Apply difference array updates
        for r1, c1, r2, c2 in queries:
            diff[r1][c1] += 1
            diff[r1][c2 + 1] -= 1
            diff[r2 + 1][c1] -= 1
            diff[r2 + 1][c2 + 1] += 1

        # Step 3: Build prefix sums horizontally
        for i in range(n):
            for j in range(1, n):
                diff[i][j] += diff[i][j - 1]

        # Step 4: Build prefix sums vertically
        for j in range(n):
            for i in range(1, n):
                diff[i][j] += diff[i - 1][j]

        # Step 5: Extract top-left n x n as result
        res = [row[:n] for row in diff[:n]]
        return res
