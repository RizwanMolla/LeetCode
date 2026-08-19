from typing import List

class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        n = len(fruits)
        prefix = [0] * (n + 1)
        
        for i in range(n):
            prefix[i + 1] = prefix[i] + fruits[i][1]
        
        maxFruit = 0
        left = 0
        
        for right in range(n):
            while left <= right:
                l_pos, r_pos = fruits[left][0], fruits[right][0]
                
                distLeftFirst = abs(startPos - l_pos) + (r_pos - l_pos)
                distRightFirst = abs(startPos - r_pos) + (r_pos - l_pos)
                
                if min(distLeftFirst, distRightFirst) <= k:
                    break
                left += 1
            
            if left <= right:
                total = prefix[right + 1] - prefix[left]
                maxFruit = max(maxFruit, total)
        
        return maxFruit
