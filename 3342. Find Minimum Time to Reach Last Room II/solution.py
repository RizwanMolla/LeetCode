from collections import deque
import heapq

class Solution:
    def minTimeToReach(self, moveTime: list[list[int]]) -> int:
        n, m = len(moveTime), len(moveTime[0])
        
        # Define directions: up, right, down, left
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        
        # Initialize a priority queue for Dijkstra's algorithm
        # Format: (current_time, row, col, move_cost)
        # move_cost alternates between 1 and 2 seconds
        pq = [(0, 0, 0, 1)]  # Start at (0,0) with time 0, next move costs 1 second
        
        # To keep track of visited states
        # We need to track (row, col, move_cost) to handle the alternating costs
        visited = set()
        
        while pq:
            current_time, row, col, move_cost = heapq.heappop(pq)
            
            # If we've reached the destination
            if row == n - 1 and col == m - 1:
                return current_time
            
            # If we've already visited this state, skip
            state = (row, col, move_cost)
            if state in visited:
                continue
            
            visited.add(state)
            
            # Try all four directions
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                
                # Check if the new position is valid
                if 0 <= new_row < n and 0 <= new_col < m:
                    # Calculate the time we can start moving to the new room
                    start_move_time = max(current_time, moveTime[new_row][new_col])
                    
                    # Calculate the time to arrive at the new room
                    arrival_time = start_move_time + move_cost
                    
                    # Calculate the next move cost (alternating between 1 and 2)
                    next_move_cost = 2 if move_cost == 1 else 1
                    
                    # Add to priority queue
                    heapq.heappush(pq, (arrival_time, new_row, new_col, next_move_cost))
        
        # If no path is found (should not happen given the constraints)
        return -1