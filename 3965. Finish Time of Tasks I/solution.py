from typing import List

class Solution:
    def finishTime(self, n: int, edges: List[List[int]], baseTime: List[int]) -> int:
        children = [[] for _ in range(n)]
        for u, v in edges:
            children[u].append(v)

        order = []
        stack = [0]

        while stack:
            u = stack.pop()
            order.append(u)
            for v in children[u]:
                stack.append(v)

        finish = [0] * n

        for u in reversed(order):
            if not children[u]:  # leaf
                finish[u] = baseTime[u]
            else:
                earliest = min(finish[v] for v in children[u])
                latest = max(finish[v] for v in children[u])

                own_duration = (latest - earliest) + baseTime[u]
                finish[u] = latest + own_duration

        return finish[0]