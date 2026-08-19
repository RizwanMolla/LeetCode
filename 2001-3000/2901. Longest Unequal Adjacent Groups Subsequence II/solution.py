from typing import List

class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        n = len(words)
        
        # Helper function to check if two words have hamming distance of 1
        def hamming_distance_is_one(word1, word2):
            # Check if words are of equal length
            if len(word1) != len(word2):
                return False
            
            # Count differences
            diff_count = 0
            for c1, c2 in zip(word1, word2):
                if c1 != c2:
                    diff_count += 1
                    if diff_count > 1:
                        return False
            
            # Return true if hamming distance is exactly 1
            return diff_count == 1
        
        # dp[i] represents the length of the longest valid subsequence ending at index i
        dp = [1] * n
        
        # prev[i] stores the previous index in the optimal subsequence ending at i
        prev = [-1] * n
        
        # Find the longest subsequence
        for i in range(1, n):
            for j in range(i):
                # Check both conditions:
                # 1. Different groups
                # 2. Hamming distance is 1 between words of equal length
                if (groups[i] != groups[j] and 
                    hamming_distance_is_one(words[i], words[j]) and 
                    dp[j] + 1 > dp[i]):
                    dp[i] = dp[j] + 1
                    prev[i] = j
        
        # Find the index with maximum dp value
        max_length = max(dp)
        end_index = dp.index(max_length)
        
        # Reconstruct the subsequence
        result = []
        while end_index != -1:
            result.append(words[end_index])
            end_index = prev[end_index]
        
        # Return the result in the correct order
        return result[::-1]