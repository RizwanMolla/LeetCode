from typing import List

class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        n = len(words)
        result = []
        
        # Handle empty input
        if n == 0:
            return result
        
        # Start with the first word
        result.append(words[0])
        last_group = groups[0]
        
        # Iterate through the rest of the words
        for i in range(1, n):
            # If the current group is different from the last group we added
            if groups[i] != last_group:
                result.append(words[i])
                last_group = groups[i]
        
        return result