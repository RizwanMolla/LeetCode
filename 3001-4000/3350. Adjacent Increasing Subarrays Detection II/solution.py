from typing import List

class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0

        end_len = [0] * n
        end_len[0] = 1
        for i in range(1, n):
            if nums[i] > nums[i-1]:
                end_len[i] = end_len[i-1] + 1
            else:
                end_len[i] = 1

        start_len = [0] * n
        start_len[n-1] = 1
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i+1]:
                start_len[i] = start_len[i+1] + 1
            else:
                start_len[i] = 1

        max_k = 0
        for j in range(1, n):
            len_A = end_len[j-1] 
            len_B = start_len[j]
            
            current_k = min(len_A, len_B)
            
            if current_k > max_k:
                max_k = current_k
        
        return max_k