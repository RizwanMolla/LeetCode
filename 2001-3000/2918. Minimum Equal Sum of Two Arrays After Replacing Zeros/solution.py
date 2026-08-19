class Solution:
    def minSum(self, nums1: list[int], nums2: list[int]) -> int:
        # Calculate the current sum and count of zeros in each array
        sum1 = sum(nums1)
        sum2 = sum(nums2)
        zeros1 = nums1.count(0)
        zeros2 = nums2.count(0)
        
        # Calculate the minimum possible sum for each array after replacing zeros
        # (Each zero must be replaced with at least 1)
        min_sum1 = sum1 + zeros1  # Current sum + minimum replacement for zeros
        min_sum2 = sum2 + zeros2  # Current sum + minimum replacement for zeros
        
        # Case 1: If there are no zeros in nums1, we can't increase its sum
        if zeros1 == 0 and min_sum1 < min_sum2:
            return -1
        
        # Case 2: If there are no zeros in nums2, we can't increase its sum
        if zeros2 == 0 and min_sum2 < min_sum1:
            return -1
        
        # Return the maximum of the minimum possible sums
        # This ensures both arrays can reach this sum by replacing zeros
        return max(min_sum1, min_sum2)