from typing import List
import heapq

class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        n, m = len(moveTime), len(moveTime[0])
        
        # After careful analysis of the examples, it seems moveTime[i][j] is the 
        # minimum time when you can START MOVING TO that room, not from it
        
        # Create a dp array to store minimum time to reach each cell
        dp = [[float('inf') for _ in range(m)] for _ in range(n)]
        dp[0][0] = 0  # Starting time at (0,0) is 0
        
        # Priority queue for Dijkstra's algorithm
        # Format: (current_time, row, col)
        pq = [(0, 0, 0)]
        
        # Directions: right, down, left, up
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        while pq:
            current_time, row, col = heapq.heappop(pq)
            
            # If we've found a better path already, skip
            if current_time > dp[row][col]:
                continue
                
            # Try all four adjacent rooms
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                
                # Check if new position is valid
                if 0 <= new_row < n and 0 <= new_col < m:
                    # We can only move to the new cell at or after moveTime[new_row][new_col]
                    earliest_move_time = max(current_time, moveTime[new_row][new_col])
                    
                    # Time to arrive at the next room (add 1 second for movement)
                    new_time = earliest_move_time + 1
                    
                    # If this is a better path, update and add to queue
                    if new_time < dp[new_row][new_col]:
                        dp[new_row][new_col] = new_time
                        heapq.heappush(pq, (new_time, new_row, new_col))
        
        return dp[n-1][m-1]