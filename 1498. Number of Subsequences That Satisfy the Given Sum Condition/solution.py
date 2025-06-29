class Solution:
    def numSubseq(self, nums: list[int], target: int) -> int:
        MOD = 10**9 + 7
        nums.sort()
        
        # Precompute powers of 2 up to len(nums)
        pow2 = [1] * len(nums)
        for i in range(1, len(nums)):
            pow2[i] = (pow2[i-1] * 2) % MOD
        
        left, right = 0, len(nums) - 1
        result = 0
        
        while left <= right:
            if nums[left] + nums[right] <= target:
                result = (result + pow2[right - left]) % MOD
                left += 1
            else:
                right -= 1
        
        return result
