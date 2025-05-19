class Solution:
    def triangleType(self, nums: list[int]) -> str:
        # Sort the array for easier triangle inequality check
        nums.sort()
        
        # Check if the three sides can form a triangle
        # Triangle inequality: sum of the lengths of any two sides must be greater than the length of the remaining side
        if nums[0] + nums[1] <= nums[2]:
            return "none"
        
        # Check if all sides are equal (equilateral)
        if nums[0] == nums[1] == nums[2]:
            return "equilateral"
        
        # Check if any two sides are equal (isosceles)
        if nums[0] == nums[1] or nums[1] == nums[2]:
            return "isosceles"
        
        # If all sides are different (scalene)
        return "scalene"