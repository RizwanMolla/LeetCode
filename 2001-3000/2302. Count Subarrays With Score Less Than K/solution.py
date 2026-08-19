class Solution:
    def countSubarrays(self, nums, k):
        n = len(nums)
        left = 0
        total = 0
        result = 0

        for right in range(n):
            total += nums[right]

            while total * (right - left + 1) >= k:
                total -= nums[left]
                left += 1

            result += (right - left + 1)

        return result
