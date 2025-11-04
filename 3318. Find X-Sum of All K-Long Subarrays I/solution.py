from collections import Counter
from typing import List

class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        ans = []
        
        for i in range(n - k + 1):
            window = nums[i:i+k]
            freq = Counter(window)
            
            # Sort by frequency descending, then value descending
            sorted_items = sorted(freq.items(), key=lambda p: (p[1], p[0]), reverse=True)
            
            # Pick top x elements
            top_x = sorted_items[:x]
            
            # Compute sum considering frequency * value
            total = sum(val * cnt for val, cnt in top_x)
            ans.append(total)
        
        return ans
