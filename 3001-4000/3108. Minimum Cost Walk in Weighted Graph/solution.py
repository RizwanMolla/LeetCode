class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def merge(self, a, b):
        pa, pb = self.find(a), self.find(b)
        if pa == pb:
            return False
        if self.rank[pa] > self.rank[pb]:
            self.parent[pb] = pa
            self.rank[pa] += self.rank[pb]
        else:
            self.parent[pa] = pb
            self.rank[pb] += self.rank[pa]
        return True

class Solution:
    def minimumCost(self, n: int, edges: list[list[int]], queries: list[list[int]]) -> list[int]:
        res = [-1] * n
        dsu = DSU(n)
        for u, v, _ in edges:
            dsu.merge(u, v)
        for u, _, w in edges:
            res[dsu.find(u)] &= w
        return [0 if s == t else res[dsu.find(s)] if dsu.find(s) == dsu.find(t) else -1 for s, t in queries]
