from typing import List

class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        self.max_or = 0
        self.count = 0
        
        def dfs(index, curr_or):
            if index == len(nums):
                if curr_or == self.max_or:
                    self.count += 1
                return
            # Include nums[index]
            dfs(index + 1, curr_or | nums[index])
            # Exclude nums[index]
            dfs(index + 1, curr_or)
        
        # Find maximum OR by OR-ing all elements (whole array is the max possible OR subset)
        self.max_or = 0
        for num in nums:
            self.max_or |= num
        
        # Start backtracking
        dfs(0, 0)
        
        return self.count
