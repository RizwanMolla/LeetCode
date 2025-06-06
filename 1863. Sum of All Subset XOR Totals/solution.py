class Solution:
    def subsetXORSum(self, nums: list[int]) -> int:
        def dfs(index, current_xor):
            if index == len(nums):
                return current_xor
            include = dfs(index + 1, current_xor ^ nums[index])
            exclude = dfs(index + 1, current_xor)
            return include + exclude
        
        return dfs(0, 0)
