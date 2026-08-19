class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Dutch national flag algorithm
        # Use three pointers: left (for 0s), right (for 2s), and current
        left, current, right = 0, 0, len(nums) - 1
        
        while current <= right:
            if nums[current] == 0:
                # Swap with the left pointer and move both pointers
                nums[left], nums[current] = nums[current], nums[left]
                left += 1
                current += 1
            elif nums[current] == 2:
                # Swap with the right pointer and move only right pointer
                nums[current], nums[right] = nums[right], nums[current]
                right -= 1
                # Don't increment current yet as the swapped element needs to be checked
            else:  # nums[current] == 1
                # No swap needed, just move current pointer
                current += 1