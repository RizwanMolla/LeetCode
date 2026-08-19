from typing import List

class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        n = len(tops)
        
        # Check if it's possible to make all tops or bottoms have the value of tops[0]
        def check_rotations(target_val):
            # Count rotations needed to make all tops equal to target_val
            top_rotations = 0
            # Count rotations needed to make all bottoms equal to target_val
            bottom_rotations = 0
            
            for i in range(n):
                # If neither top nor bottom matches target_val, it's impossible
                if tops[i] != target_val and bottoms[i] != target_val:
                    return -1
                
                # Count rotations needed for tops
                if tops[i] != target_val:
                    top_rotations += 1
                
                # Count rotations needed for bottoms
                if bottoms[i] != target_val:
                    bottom_rotations += 1
            
            # Return the minimum rotations needed
            return min(top_rotations, bottom_rotations)
        
        # Try with the value of tops[0]
        rotations = check_rotations(tops[0])
        if rotations != -1:
            return rotations
        
        # If tops[0] doesn't work, try with bottoms[0]
        # Only need to check if tops[0] != bottoms[0]
        if tops[0] != bottoms[0]:
            return check_rotations(bottoms[0])
        
        # If both attempts fail, it's impossible
        return -1