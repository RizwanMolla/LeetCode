class Solution:
    def check(self, nums: list[int]) -> bool:
        count = 0
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                count += 1
                if count > 1:
                    return False
        return count == 0 or nums[-1] <= nums[0]