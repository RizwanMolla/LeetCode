class Solution:
    def dfs(self, adj, values, k, cnt, cur, par=-1):
        total = values[cur]
        for nbr in adj[cur]:
            if nbr != par:
                total += self.dfs(adj, values, k, cnt, nbr, cur)
        total %= k
        if total == 0:
            cnt[0] += 1
        return total

    def maxKDivisibleComponents(self, n, edges, values, k):
        from collections import defaultdict
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        cnt = [0]
        self.dfs(adj, values, k, cnt, 0)
        return cnt[0]
