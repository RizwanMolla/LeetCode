from bisect import bisect_left
from math import ceil

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        # Sort potions to perform binary search
        potions.sort()
        m = len(potions)
        result = []

        for spell in spells:
            # Minimum required potion strength for success
            required = (success + spell - 1) // spell  # same as ceil(success / spell)

            # Find index using binary search
            idx = bisect_left(potions, required)

            # Count of successful potions = potions from idx to end
            count = m - idx
            result.append(count)

        return result
