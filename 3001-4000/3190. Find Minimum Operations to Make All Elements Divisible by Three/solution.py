class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        operations = 0
        for x in nums:
            if x % 3 != 0:
                operations += 1
        return operations
