class Solution:
    def maxTargetNodes(
        self, edges1: list[list[int]], edges2: list[list[int]]
    ) -> list[int]:
        def build_adjacency_list(edges: list[list[int]]) -> list[list[int]]:
            num_nodes = len(edges) + 1
            adjacency_list = [[] for _ in range(num_nodes)]
            for node_a, node_b in edges:
                adjacency_list[node_a].append(node_b)
                adjacency_list[node_b].append(node_a)
            return adjacency_list
        
        def dfs_bipartite_coloring(
            graph: list[list[int]], 
            current_node: int, 
            parent_node: int, 
            node_colors: list[int], 
            current_color: int, 
            color_counts: list[int]
        ):
            node_colors[current_node] = current_color
            color_counts[current_color] += 1
            for neighbor in graph[current_node]:
                if neighbor != parent_node:
                    dfs_bipartite_coloring(
                        graph, neighbor, current_node, node_colors, 
                        current_color ^ 1, color_counts
                    )
        
        graph1 = build_adjacency_list(edges1)
        graph2 = build_adjacency_list(edges2)
        
        nodes_count1, nodes_count2 = len(graph1), len(graph2)
        
        node_colors1 = [0] * nodes_count1
        node_colors2 = [0] * nodes_count2
        color_counts1 = [0, 0]
        color_counts2 = [0, 0]
        
        # Color the second graph to find the maximum bipartite set
        dfs_bipartite_coloring(graph2, 0, -1, node_colors2, 0, color_counts2)
        # Color the first graph
        dfs_bipartite_coloring(graph1, 0, -1, node_colors1, 0, color_counts1)
        
        # Get the maximum count from the second graph
        max_targets_from_graph2 = max(color_counts2)
        
        # For each node in graph1, add its bipartite set count to max from graph2
        return [max_targets_from_graph2 + color_counts1[node_colors1[node_index]] 
                for node_index in range(nodes_count1)]