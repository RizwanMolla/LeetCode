class Solution:
    def maxAscendingSum(self, nums: list[int]) -> int:
        if not nums:
            return 0
        
        max_sum = nums[0]
        current_sum = nums[0]
        
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                current_sum += nums[i]
            else:
                if current_sum > max_sum:
                    max_sum = current_sum
                current_sum = nums[i]
        
        if current_sum > max_sum:
            max_sum = current_sum
        
        return max_sum