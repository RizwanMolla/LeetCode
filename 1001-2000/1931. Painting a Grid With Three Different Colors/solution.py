class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        MOD = 10**9 + 7
        
        # Generate all possible valid column states
        # Each state is represented as an integer where each pair of bits represents a color
        # 0 = red, 1 = green, 2 = blue
        valid_states = []
        
        # Helper function to check if a column configuration is valid (no adjacent cells with the same color)
        def is_valid_column(state):
            colors = []
            for _ in range(m):
                colors.append(state % 3)
                state //= 3
            
            for i in range(1, m):
                if colors[i] == colors[i-1]:
                    return False
            return True
        
        # Generate all possible column states
        def generate_states(pos, state):
            if pos == m:
                if is_valid_column(state):
                    valid_states.append(state)
                return
            
            for color in range(3):  # 0: red, 1: green, 2: blue
                next_state = state + (color * (3 ** pos))
                generate_states(pos + 1, next_state)
        
        generate_states(0, 0)
        
        # Build adjacency list: which states can be adjacent to each other
        adj = {}
        for state in valid_states:
            adj[state] = []
        
        # Two columns can be adjacent if no row has the same color in both columns
        for state1 in valid_states:
            for state2 in valid_states:
                colors1 = [0] * m
                colors2 = [0] * m
                
                temp1, temp2 = state1, state2
                for i in range(m):
                    colors1[i] = temp1 % 3
                    colors2[i] = temp2 % 3
                    temp1 //= 3
                    temp2 //= 3
                
                valid = True
                for i in range(m):
                    if colors1[i] == colors2[i]:
                        valid = False
                        break
                
                if valid:
                    adj[state1].append(state2)
        
        # Initialize DP array
        dp = {}
        for state in valid_states:
            dp[state] = 1  # One way to color a single column
        
        # Build up the solution column by column
        for col in range(1, n):
            new_dp = {}
            for state in valid_states:
                new_dp[state] = 0
                for prev_state in adj[state]:
                    new_dp[state] = (new_dp[state] + dp[prev_state]) % MOD
            dp = new_dp
        
        # Sum up all possible ways to color the grid
        return sum(dp.values()) % MOD