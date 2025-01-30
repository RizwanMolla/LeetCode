from collections import defaultdict, deque

class Solution:
    def magnificentSets(self, n: int, edges: list[list[int]]) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = [False] * (n + 1)
        max_groups = 0

        for node in range(1, n + 1):
            if not visited[node]:
                component = []
                queue = deque([node])
                visited[node] = True
                while queue:
                    u = queue.popleft()
                    component.append(u)
                    for v in graph[u]:
                        if not visited[v]:
                            visited[v] = True
                            queue.append(v)

                max_group_for_component = 0
                for start in component:
                    group = {}
                    queue = deque([(start, 1)])
                    group[start] = 1
                    valid = True
                    while queue:
                        u, g = queue.popleft()
                        for v in graph[u]:
                            if v not in group:
                                group[v] = g + 1
                                queue.append((v, g + 1))
                            elif abs(group[v] - g) != 1:
                                valid = False
                                break
                        if not valid:
                            break
                    if valid:
                        max_group_for_component = max(max_group_for_component, max(group.values()))

                if max_group_for_component == 0:
                    return -1
                max_groups += max_group_for_component

        return max_groups