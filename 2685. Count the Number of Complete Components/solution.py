from typing import List

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        from collections import defaultdict, deque

        graph = defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)

        visited = set()
        complete_count = 0

        def bfs(start):
            queue = deque([start])
            component = set()
            edge_count = 0

            while queue:
                node = queue.popleft()
                if node in visited:
                    continue
                visited.add(node)
                component.add(node)

                for neighbor in graph[node]:
                    if neighbor not in visited:
                        queue.append(neighbor)
                    edge_count += 1

            return component, edge_count // 2  

        for node in range(n):
            if node not in visited:
                component, edge_count = bfs(node)
                size = len(component)
                
                if edge_count == size * (size - 1) // 2:
                    complete_count += 1

        return complete_count
