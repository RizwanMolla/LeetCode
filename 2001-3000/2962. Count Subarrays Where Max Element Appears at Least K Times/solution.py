class Solution:
    def countSubarrays(self, nums: list[int], k: int) -> int:
        max_val = max(nums)
        left = 0
        count = 0
        freq = 0
        res = 0
        
        for right in range(len(nums)):
            if nums[right] == max_val:
                freq += 1

            while freq >= k:
                res += len(nums) - right
                if nums[left] == max_val:
                    freq -= 1
                left += 1

        return res
