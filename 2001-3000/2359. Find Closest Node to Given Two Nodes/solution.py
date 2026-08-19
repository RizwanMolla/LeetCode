class Solution:
    def closestMeetingNode(self, edges: list[int], node1: int, node2: int) -> int:
        def get_distances(start):
            n = len(edges)
            dist = [-1] * n
            visited = set()
            current = start
            d = 0
            while current != -1 and current not in visited:
                dist[current] = d
                visited.add(current)
                current = edges[current]
                d += 1
            return dist

        dist1 = get_distances(node1)
        dist2 = get_distances(node2)

        min_dist = float('inf')
        answer = -1

        for i in range(len(edges)):
            if dist1[i] != -1 and dist2[i] != -1:
                max_dist = max(dist1[i], dist2[i])
                if max_dist < min_dist:
                    min_dist = max_dist
                    answer = i

        return answer
