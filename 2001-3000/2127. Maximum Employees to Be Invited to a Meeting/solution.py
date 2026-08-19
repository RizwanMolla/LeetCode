from collections import deque

class Solution:
    def processChains(self, favorite, indegree, visited, start):
        queue = deque([start])
        last_node = -1

        while queue:
            current = queue.popleft()
            visited[current] = True
            last_node = current

            next_fav = favorite[current]
            indegree[next_fav] -= 1
            if indegree[next_fav] == 0 and not visited[next_fav]:
                queue.append(next_fav)

        return favorite[last_node]

    def calculateMaxDepth(self, reverse_fav, global_visited, n, start, exclude):
        visited = [False] * n
        queue = deque([start])
        visited[start] = visited[exclude] = True

        depth = 0
        while queue:
            for _ in range(len(queue)):
                current = queue.popleft()
                global_visited[current] = True

                for neighbor in reverse_fav[current]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        queue.append(neighbor)
            depth += 1
        return depth

    def detectCycleSize(self, favorite, visited, start):
        queue = deque([start])
        visited[start] = True

        size = 0
        while queue:
            current = queue.popleft()

            if not visited[favorite[current]]:
                visited[favorite[current]] = True
                queue.append(favorite[current])
            size += 1
        return size

    def maximumInvitations(self, favorite):
        n = len(favorite)
        reverse_fav = [[] for _ in range(n)]
        indegree = [0] * n

        for i in range(n):
            reverse_fav[favorite[i]].append(i)
            indegree[favorite[i]] += 1

        total_chain_length = 0
        visited = [False] * n

        for i in range(n):
            if indegree[i] == 0 and not visited[i]:
                last_node = self.processChains(favorite, indegree, visited, i)
                if favorite[favorite[last_node]] == last_node:
                    chain_length = self.calculateMaxDepth(reverse_fav, visited, n, last_node, favorite[last_node]) - 1
                    total_chain_length += chain_length
                    visited[last_node] = False

        two_node_cycle_count = 0
        max_cycle_length = 0

        for i in range(n):
            if not visited[i]:
                cycle_length = self.detectCycleSize(favorite, visited, i)
                if cycle_length == 2:
                    two_node_cycle_count += 1
                else:
                    max_cycle_length = max(max_cycle_length, cycle_length)

        max_two_node_cycle_length = total_chain_length + 2 * two_node_cycle_count
        return max(max_two_node_cycle_length, max_cycle_length)
