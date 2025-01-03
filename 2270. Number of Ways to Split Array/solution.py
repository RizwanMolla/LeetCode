class Solution(object):
    def waysToSplitArray(self, nums):
        total_sum = sum(nums)
        left_sum = 0
        count = 0
        for i in range(len(nums) - 1):
            left_sum += nums[i]
            if left_sum >= total_sum - left_sum:
                count += 1
        return count


"""
Summary:
The solution uses a single pass to compute the valid splits. We maintain the cumulative left_sum and compare it with total_sum - left_sum for each index, excluding the last index as per constraints. This ensures an O(n) time complexity and O(1) space complexity.
"""