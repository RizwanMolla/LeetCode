from typing import List

class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        EPSILON = 1e-6  # tolerance for floating point errors
        TARGET = 24
        
        def dfs(nums):
            # Base case: only one number left
            if len(nums) == 1:
                return abs(nums[0] - TARGET) < EPSILON
            
            # Try all pairs of numbers
            for i in range(len(nums)):
                for j in range(len(nums)):
                    if i == j:
                        continue
                    
                    # Remaining numbers after picking i and j
                    next_nums = [nums[k] for k in range(len(nums)) if k != i and k != j]
                    
                    # Try all operations
                    for result in compute(nums[i], nums[j]):
                        if dfs(next_nums + [result]):
                            return True
            return False
        
        def compute(a, b):
            results = [a + b, a - b, b - a, a * b]
            if abs(b) > EPSILON:  # avoid division by zero
                results.append(a / b)
            if abs(a) > EPSILON:
                results.append(b / a)
            return results
        
        return dfs([float(x) for x in cards])
