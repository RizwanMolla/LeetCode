from collections import deque
from typing import List

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        """
        Find minimum dice rolls to reach the last square using BFS.
        
        Time: O(n²) - each square visited at most once
        Space: O(n²) - for the queue and visited set
        """
        n = len(board)
        target = n * n
        
        def getCoordinates(square):
            """Convert square number to (row, col) coordinates"""
            # Square numbers start from 1, so adjust to 0-based
            square -= 1
            row = n - 1 - square // n  # Bottom to top
            col = square % n
            
            # Handle boustrophedon (alternating direction)
            # Odd rows (from bottom) go right-to-left
            if (n - 1 - row) % 2 == 1:
                col = n - 1 - col
                
            return row, col
        
        # BFS to find minimum moves
        queue = deque([(1, 0)])  # (current_square, moves)
        visited = {1}
        
        while queue:
            curr_square, moves = queue.popleft()
            
            # Try all possible dice rolls (1-6)
            for dice in range(1, 7):
                next_square = curr_square + dice
                
                # Don't go beyond the board
                if next_square > target:
                    break
                
                # Get coordinates for this square
                row, col = getCoordinates(next_square)
                
                # Check if there's a snake or ladder
                if board[row][col] != -1:
                    next_square = board[row][col]
                
                # If we reached the target
                if next_square == target:
                    return moves + 1
                
                # If not visited, add to queue
                if next_square not in visited:
                    visited.add(next_square)
                    queue.append((next_square, moves + 1))
        
        return -1  # Cannot reach target