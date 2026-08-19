class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        # Edge Case: Repunits (1, 11, 111...) are never divisible by 2 or 5.
        if k % 2 == 0 or k % 5 == 0:
            return -1
        
        remainder = 0
        
        # By Pigeonhole Principle, if a solution exists, 
        # it must be found within 'k' iterations.
        for length in range(1, k + 1):
            remainder = (remainder * 10 + 1) % k
            if remainder == 0:
                return length
                
        return -1