class Solution:
    def numTilings(self, n: int) -> int:
        """
        Count the number of ways to tile a 2×n board with dominoes and trominoes.
        
        Args:
            n: The width of the 2×n board
            
        Returns:
            The number of ways to tile the board, modulo 10^9 + 7
        """
        MOD = 10**9 + 7
        
        # Base cases
        if n <= 2:
            return n
        if n == 3:
            return 5
        
        # Initialize dp arrays
        # full[i] = number of ways to completely tile a 2×i board
        # partial[i] = number of ways to tile a 2×i board with top-right or bottom-right corner missing
        full = [0] * (n + 1)
        partial = [0] * (n + 1)
        
        # Set base cases
        full[1] = 1  # One way to tile a 2×1 board (with a single domino)
        full[2] = 2  # Two ways to tile a 2×2 board (two vertical or two horizontal dominoes)
        partial[1] = 0  # Cannot have a partial tiling for a 2×1 board
        partial[2] = 1  # One way to have a partial tiling for a 2×2 board
        
        # Fill the dp arrays
        for i in range(3, n + 1):
            # For a fully tiled board, we can:
            # 1. Add a vertical domino to a fully tiled (i-1) board
            # 2. Add two horizontal dominoes to a fully tiled (i-2) board
            # 3. Add a tromino to each of the two possible partial tilings of (i-1)
            full[i] = (full[i-1] + full[i-2] + 2 * partial[i-1]) % MOD
            
            # For a partially tiled board, we can:
            # 1. Add a horizontal domino to a partially tiled (i-1) board
            # 2. Add a tromino to a fully tiled (i-2) board
            partial[i] = (partial[i-1] + full[i-2]) % MOD
        
        return full[n]