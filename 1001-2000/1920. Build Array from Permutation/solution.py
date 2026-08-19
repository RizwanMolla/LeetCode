class Solution:
    def buildArray(self, nums: list[int]) -> list[int]:
        ans = [nums[nums[i]] for i in range(len(nums))]
        return ans