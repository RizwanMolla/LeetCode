from typing import List

class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        # Check if array has less than 3 elements
        if len(arr) < 3:
            return False
        
        # Iterate through the array until the third-to-last element
        for i in range(len(arr) - 2):
            # Check if current and next two elements are all odd
            if arr[i] % 2 == 1 and arr[i+1] % 2 == 1 and arr[i+2] % 2 == 1:
                return True
        
        # If we didn't find three consecutive odds
        return False