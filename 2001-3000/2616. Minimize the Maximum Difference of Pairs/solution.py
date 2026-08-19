from typing import List

class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        if p == 0:
            return 0
        
        nums.sort()  # Sort to enable greedy pairing of adjacent elements
        n = len(nums)
        
        def canFormPairs(maxDiff):
            """Check if we can form at least p pairs with max difference <= maxDiff"""
            pairs = 0
            i = 0
            
            while i < n - 1:
                # If current adjacent pair has difference <= maxDiff, form the pair
                if nums[i + 1] - nums[i] <= maxDiff:
                    pairs += 1
                    i += 2  # Skip both elements as they're now paired
                else:
                    i += 1  # Move to next element
                
                if pairs >= p:  # Early termination
                    return True
            
            return pairs >= p
        
        # Binary search on the maximum difference
        left, right = 0, nums[-1] - nums[0]
        result = right
        
        while left <= right:
            mid = (left + right) // 2
            
            if canFormPairs(mid):
                result = mid  # This max difference works, try smaller
                right = mid - 1
            else:
                left = mid + 1  # Need larger max difference
        
        return result
