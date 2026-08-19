class Solution:
    def maximumDifference(self, nums: list[int]) -> int:
        """
        Find maximum difference nums[j] - nums[i] where i < j and nums[i] < nums[j].
        
        Approach:
        - Keep track of minimum element seen so far
        - For each element, calculate difference with minimum
        - Only consider positive differences (nums[i] < nums[j])
        
        Time: O(n), Space: O(1)
        """
        max_diff = -1
        min_so_far = nums[0]
        
        for i in range(1, len(nums)):
            # If current element is greater than minimum so far,
            # we have a valid increasing pair
            if nums[i] > min_so_far:
                max_diff = max(max_diff, nums[i] - min_so_far)
            
            # Update minimum for future iterations
            min_so_far = min(min_so_far, nums[i])
        
        return max_diff