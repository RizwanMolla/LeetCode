from collections import defaultdict
from typing import List

class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        bob_time = {}
        def find_bob_path(node, parent, depth):
            if node == 0:
                bob_time[node] = depth
                return True
            for neighbor in graph[node]:
                if neighbor != parent and find_bob_path(neighbor, node, depth + 1):
                    bob_time[node] = depth
                    return True
            return False

        find_bob_path(bob, -1, 0)

        def dfs(node, parent, depth):
            if node in bob_time:
                if bob_time[node] > depth:
                    val = amount[node]
                elif bob_time[node] == depth:
                    val = amount[node] // 2
                else:
                    val = 0
            else:
                val = amount[node]

            if len(graph[node]) == 1 and node != 0:
                return val

            max_profit = float('-inf')
            for neighbor in graph[node]:
                if neighbor != parent:
                    max_profit = max(max_profit, dfs(neighbor, node, depth + 1))
                    
            return val + max_profit

        return dfs(0, -1, 0)
