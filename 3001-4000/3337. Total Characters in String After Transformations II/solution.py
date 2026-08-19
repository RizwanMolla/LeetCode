from typing import List
class Solution:
    def lengthAfterTransformations(self, s: str, t: int, nums: List[int]) -> int:
        MOD = 10**9 + 7
        
        # Convert the string to character counts
        char_counts = [0] * 26
        for char in s:
            char_counts[ord(char) - ord('a')] += 1
        
        # If t is large, we need an efficient approach
        if t > 0:
            # For each character position, calculate how it transforms
            # Create a 26x26 transition matrix
            # transition[i][j] = how many characters j a single character i produces after one transformation
            transition = [[0] * 26 for _ in range(26)]
            
            for i in range(26):  # For each starting character (a to z)
                count = nums[i]  # How many next characters it transforms into
                for j in range(count):
                    next_char = (i + j + 1) % 26  # The next character in sequence
                    transition[i][next_char] += 1
            
            # Fast matrix exponentiation to get transition^t
            transition_t = self.matrix_power(transition, t, MOD)
            
            # Calculate the final counts
            final_counts = [0] * 26
            for i in range(26):  # For each original character
                for j in range(26):  # For each possible resulting character
                    # Add the contribution of this original character to the final counts
                    final_counts[j] = (final_counts[j] + char_counts[i] * transition_t[i][j]) % MOD
            
            # Sum up to get the total length
            total_length = sum(final_counts) % MOD
            return total_length
        else:
            # If t = 0, just return the original length
            return len(s) % MOD
    
    def matrix_power(self, matrix, power, mod):
        """
        Calculate matrix^power % mod using fast exponentiation
        """
        n = len(matrix)
        # Initialize result as identity matrix
        result = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
        
        # Binary exponentiation
        while power > 0:
            if power & 1:  # If the current bit is 1
                result = self.matrix_multiply(result, matrix, mod)
            matrix = self.matrix_multiply(matrix, matrix, mod)
            power >>= 1
        
        return result
    
    def matrix_multiply(self, A, B, mod):
        """
        Multiply two matrices A and B and take modulo mod
        """
        n = len(A)
        C = [[0] * n for _ in range(n)]
        
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    C[i][j] = (C[i][j] + A[i][k] * B[k][j]) % mod
        
        return C