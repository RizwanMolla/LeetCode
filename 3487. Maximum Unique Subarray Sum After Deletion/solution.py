class Solution:
    def maxSum(self, nums: list[int]) -> int:
        
        unique_elements = set()
        for num in nums:
            unique_elements.add(num)
        
        total_unique_positive_sum = 0
        for x in unique_elements:
            if x > 0:
                total_unique_positive_sum += x
    
        if total_unique_positive_sum > 0:
            return total_unique_positive_sum
        else:
            return max(nums)