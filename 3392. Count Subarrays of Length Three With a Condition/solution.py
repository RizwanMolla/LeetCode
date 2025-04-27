class Solution:
    def countSubarrays(self, nums: list[int]) -> int:
        count = 0
        
        for i in range(len(nums) - 2):
            first = nums[i]
            second = nums[i + 1]
            third = nums[i + 2]
            
            if second % 2 == 0 and first + third == second // 2:
                count += 1
        
        return count
