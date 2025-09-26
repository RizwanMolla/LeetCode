from typing import List

class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        count = 0
        
        for i in range(n-1, 1, -1):  # fix largest side
            l, r = 0, i - 1
            while l < r:
                if nums[l] + nums[r] > nums[i]:
                    count += (r - l)  # all pairs (l..r-1, r) are valid
                    r -= 1
                else:
                    l += 1
        return count
