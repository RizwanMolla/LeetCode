from typing import List
from collections import defaultdict

class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        # Use a dictionary to count the frequency of each normalized domino
        domino_count = defaultdict(int)
        pairs = 0
        
        for domino in dominoes:
            # Normalize the domino by ensuring the smaller number is first
            # This handles the rotation equivalence
            normalized = tuple(sorted(domino))
            
            # Add the count of existing matching dominoes to our pairs
            # For each new domino, if we've seen n of the same kind before,
            # it forms n new pairs
            pairs += domino_count[normalized]
            
            # Increment the count for this normalized domino
            domino_count[normalized] += 1
        
        return pairs