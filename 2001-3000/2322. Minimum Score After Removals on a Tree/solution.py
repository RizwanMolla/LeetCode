from typing import List
from collections import defaultdict

class Solution:
    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:
        n = len(nums)
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        in_time = [0] * n
        out_time = [0] * n
        xor = [0] * n
        time = 0

        # DFS to compute subtree XOR and in/out times
        def dfs(node, parent):
            nonlocal time
            in_time[node] = time
            time += 1
            xor[node] = nums[node]
            for nei in graph[node]:
                if nei != parent:
                    dfs(nei, node)
                    xor[node] ^= xor[nei]
            out_time[node] = time
            time += 1

        dfs(0, -1)
        total_xor = xor[0]

        # Check if u is ancestor of v
        def is_ancestor(u, v):
            return in_time[u] <= in_time[v] and out_time[v] <= out_time[u]

        min_score = float('inf')

        # Convert undirected edges into parent -> child using in-time
        directed_edges = []
        for u, v in edges:
            if in_time[u] < in_time[v]:
                directed_edges.append((u, v))
            else:
                directed_edges.append((v, u))

        for i in range(len(directed_edges)):
            for j in range(i + 1, len(directed_edges)):
                a, b = directed_edges[i]
                c, d = directed_edges[j]

                if is_ancestor(b, d):
                    # d is inside b's subtree
                    x = xor[d]
                    y = xor[b] ^ xor[d]
                    z = total_xor ^ xor[b]
                elif is_ancestor(d, b):
                    # b is inside d's subtree
                    x = xor[b]
                    y = xor[d] ^ xor[b]
                    z = total_xor ^ xor[d]
                else:
                    # disjoint
                    x = xor[b]
                    y = xor[d]
                    z = total_xor ^ xor[b] ^ xor[d]

                max_x = max(x, y, z)
                min_x = min(x, y, z)
                min_score = min(min_score, max_x - min_x)

        return min_score
