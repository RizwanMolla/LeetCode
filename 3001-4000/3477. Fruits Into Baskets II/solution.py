from typing import List

class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(fruits)
        used = [False] * n  # Keep track of used baskets
        unplaced = 0
        
        for fruit in fruits:
            placed = False
            for i in range(n):
                if not used[i] and baskets[i] >= fruit:
                    used[i] = True  # Mark this basket as used
                    placed = True
                    break
            if not placed:
                unplaced += 1  # Couldn't place this fruit
        
        return unplaced
