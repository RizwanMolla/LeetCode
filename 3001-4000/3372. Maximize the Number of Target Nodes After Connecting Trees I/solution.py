from typing import List

class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        def build_graph(edges: List[List[int]]) -> List[List[int]]:
            size = len(edges) + 1
            graph = [[] for _ in range(size)]
            for u, v in edges:
                graph[u].append(v)
                graph[v].append(u)
            return graph

        def count_within_k(graph: List[List[int]], node: int, parent: int, depth: int) -> int:
            if depth < 0:
                return 0
            count = 1
            for neighbor in graph[node]:
                if neighbor != parent:
                    count += count_within_k(graph, neighbor, node, depth - 1)
            return count

        # Build graphs
        tree1 = build_graph(edges1)
        tree2 = build_graph(edges2)

        # Precompute maximum reachability from any node in tree2 within (k - 1) steps
        max_reach_tree2 = max(count_within_k(tree2, node, -1, k - 1) for node in range(len(tree2)))

        # Compute result for each node in tree1
        return [
            count_within_k(tree1, node, -1, k) + max_reach_tree2
            for node in range(len(tree1))
        ]
