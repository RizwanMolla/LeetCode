class Solution:
    def numberOfArrays(self, differences: list[int], lower: int, upper: int) -> int:
        min_prefix = max_prefix = prefix = 0
        
        for diff in differences:
            prefix += diff
            min_prefix = min(min_prefix, prefix)
            max_prefix = max(max_prefix, prefix)
        
        return max(0, (upper - max_prefix) - (lower - min_prefix) + 1)
