class Solution:
    def minimumOperations(self, nums: list[int]) -> int:
        from collections import Counter
        
        operations = 0
        i = 0

        while i < len(nums):
            counter = Counter(nums[i:])
            if len(counter) == len(nums[i:]):
                break
            operations += 1
            i += 3

        return operations
