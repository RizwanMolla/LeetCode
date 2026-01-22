from typing import List

class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        def is_non_decreasing(arr):
            return all(arr[i] >= arr[i - 1] for i in range(1, len(arr)))
        
        operations = 0
        
        while not is_non_decreasing(nums):
            min_sum = float('inf')
            idx = 0
            
            for i in range(len(nums) - 1):
                pair_sum = nums[i] + nums[i + 1]
                if pair_sum < min_sum:
                    min_sum = pair_sum
                    idx = i
            
            nums = nums[:idx] + [min_sum] + nums[idx + 2:]
            operations += 1
        
        return operations
