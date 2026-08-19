from typing import List

class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Pair value with index
        indexed_nums = list(enumerate(nums))
        
        # Step 2: Sort by value descending
        sorted_by_value = sorted(indexed_nums, key=lambda x: x[1], reverse=True)
        
        # Step 3: Take top k elements
        top_k = sorted_by_value[:k]
        
        # Step 4: Sort top k by original index to preserve order
        top_k_sorted_by_index = sorted(top_k, key=lambda x: x[0])
        
        # Step 5: Return the values
        return [num for index, num in top_k_sorted_by_index]
