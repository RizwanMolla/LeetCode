from typing import List

class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        n = len(nums)
        
        # Calculate the benefit of XORing each node with k
        benefits = []
        original_sum = 0
        
        for i in range(n):
            original_val = nums[i]
            xor_val = nums[i] ^ k
            benefit = xor_val - original_val
            benefits.append(benefit)
            original_sum += original_val
        
        # Sort benefits in descending order
        benefits.sort(reverse=True)
        
        max_additional_benefit = 0
        current_benefit = 0
        
        # Try taking even numbers of nodes (0, 2, 4, 6, ...)
        # We can take 0 nodes (no operations)
        max_additional_benefit = 0
        
        # Try taking pairs of nodes with highest benefits
        for i in range(0, n, 2):
            if i + 1 < n:
                # Take pair i and i+1
                pair_benefit = benefits[i] + benefits[i + 1]
                current_benefit += pair_benefit
                if current_benefit > max_additional_benefit:
                    max_additional_benefit = current_benefit
            else:
                # Odd number of positive benefits case
                # We have i nodes so far, now we need one more to make it even
                # But we can't take just one more, so we evaluate if it's worth it
                break
        
        return original_sum + max_additional_benefit