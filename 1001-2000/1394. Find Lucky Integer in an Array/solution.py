from collections import Counter

class Solution:
    def findLucky(self, arr: list[int]) -> int:
        freq = Counter(arr)
        max_lucky = -1
        
        for num, count in freq.items():
            if num == count:
                max_lucky = max(max_lucky, num)
        
        return max_lucky
