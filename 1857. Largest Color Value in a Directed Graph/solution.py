from collections import defaultdict, deque

class Solution:
    def largestPathValue(self, colors: str, edges: list[list[int]]) -> int:
        n = len(colors)
        graph = defaultdict(list)
        indegree = [0] * n

        # Build graph and indegree
        for u, v in edges:
            graph[u].append(v)
            indegree[v] += 1

        # Queue for topological sort
        q = deque()
        for i in range(n):
            if indegree[i] == 0:
                q.append(i)

        # dp[i][c] = max number of color 'c' on path ending at node i
        dp = [[0] * 26 for _ in range(n)]
        for i in range(n):
            dp[i][ord(colors[i]) - ord('a')] = 1

        visited = 0
        res = 0

        while q:
            u = q.popleft()
            visited += 1
            for v in graph[u]:
                for c in range(26):
                    # Carry forward the max color counts
                    dp[v][c] = max(dp[v][c], dp[u][c] + (1 if c == ord(colors[v]) - ord('a') else 0))
                indegree[v] -= 1
                if indegree[v] == 0:
                    q.append(v)
            res = max(res, max(dp[u]))

        return res if visited == n else -1
