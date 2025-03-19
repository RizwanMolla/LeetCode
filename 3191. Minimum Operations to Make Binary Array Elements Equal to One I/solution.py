class Solution:
    def minOperations(self, nums: list[int]) -> int:
        n = len(nums)
        operations = 0
        
        for i in range(n - 2):
            if nums[i] == 0:
                for j in range(i, i + 3):
                    nums[j] = 1 - nums[j]  
                operations += 1
        
        if all(x == 1 for x in nums):
            return operations
        else:
            return -1
