class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        res = -1
        for i, n in enumerate(nums):
            digit_sum = sum(map(int, str(n)))
            if i == digit_sum:
                res = i
                break
        
        return res