class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        """
        Find number of ways to distribute n candies among 3 children 
        such that no child gets more than limit candies.
        
        Uses inclusion-exclusion principle with stars and bars combinatorics.
        
        Time Complexity: O(1) - constant time operations
        Space Complexity: O(1) - constant space
        """
        
        def combination(n: int, k: int) -> int:
            """Calculate C(n, k) = n! / (k! * (n-k)!)"""
            if k < 0 or k > n:
                return 0
            if k == 0 or k == n:
                return 1
            
            # Use the property C(n, k) = C(n, n-k) to minimize calculations
            k = min(k, n - k)
            
            result = 1
            for i in range(k):
                result = result * (n - i) // (i + 1)
            
            return result
        
        # Using inclusion-exclusion principle:
        # Total ways without constraint - Ways where at least one child exceeds limit
        # + Ways where at least two children exceed limit - Ways where all three exceed limit
        
        # Total ways to distribute n candies among 3 children (stars and bars)
        # This is equivalent to finding non-negative integer solutions to x1 + x2 + x3 = n
        # Answer is C(n + 3 - 1, 3 - 1) = C(n + 2, 2)
        total = combination(n + 2, 2)
        
        # Subtract cases where at least one child gets more than limit candies
        # If child i gets at least (limit + 1) candies, we distribute remaining among 3 children
        # Remaining candies = n - (limit + 1)
        if n >= limit + 1:
            # 3 ways to choose which child exceeds the limit
            exceed_one = 3 * combination(n - limit + 1, 2)
            total -= exceed_one
        
        # Add back cases where at least two children exceed limit (over-subtracted)
        if n >= 2 * (limit + 1):
            # 3 ways to choose which 2 children exceed the limit
            exceed_two = 3 * combination(n - 2 * limit, 2)
            total += exceed_two
        
        # Subtract cases where all three children exceed limit
        if n >= 3 * (limit + 1):
            # Only 1 way for all three to exceed
            exceed_three = combination(n - 3 * limit - 1, 2)
            total -= exceed_three
        
        return total