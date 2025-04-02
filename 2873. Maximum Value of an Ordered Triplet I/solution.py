from typing import List
class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        max_value = 0
        
        for j in range(1, n - 1):
            max_i = max(nums[:j])  # Maximum value before j
            max_k = max(nums[j+1:])  # Maximum value after j
            max_value = max(max_value, (max_i - nums[j]) * max_k)
        
        return max_value