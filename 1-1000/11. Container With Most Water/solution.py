from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_area = 0
        
        while left < right:
            # Calculate area
            width = right - left
            min_height = min(height[left], height[right])
            area = width * min_height
            max_area = max(max_area, area)
            
            # Move the pointer pointing to smaller height
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_area
