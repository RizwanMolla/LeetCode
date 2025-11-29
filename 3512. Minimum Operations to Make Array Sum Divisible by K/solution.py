class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        
        initial_sum = sum(nums)
        
        remainder = initial_sum % k
        
        return remainder