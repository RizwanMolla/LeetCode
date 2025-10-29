class Solution:
    def smallestNumber(self, n: int) -> int:
        x = 1
        
        while x < n:
            # Construct the next number in the sequence 2^k - 1
            # x = (x * 2) + 1, implemented using bitwise shift and OR
            x = (x << 1) | 1
            
        return x