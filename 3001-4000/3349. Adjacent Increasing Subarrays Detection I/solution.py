class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        
        def is_increasing(subarr):
            return all(subarr[i] < subarr[i+1] for i in range(len(subarr)-1))
        
        for i in range(n - 2 * k + 1):
            if is_increasing(nums[i:i+k]) and is_increasing(nums[i+k:i+2*k]):
                return True
        
        return False
