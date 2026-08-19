class Solution:
    def minCapability(self, nums: list[int], k: int) -> int:
        def canRob(k, cap):
            count = 0
            i = 0
            while i < len(nums):
                if nums[i] <= cap:
                    count += 1
                    i += 1 
                i += 1
            return count >= k

        low, high = min(nums), max(nums)
        while low < high:
            mid = (low + high) // 2
            if canRob(k, mid):
                high = mid  
            else:
                low = mid + 1
        return low
