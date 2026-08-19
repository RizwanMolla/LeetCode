from typing import List

class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        heights = [0] * n
        total = 0
        
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    heights[j] = 0
                else:
                    heights[j] += 1
            
            stack = []
            row_count = [0] * n
            for j in range(n):
                while stack and heights[stack[-1]] >= heights[j]:
                    stack.pop()
                
                if stack:
                    prev_index = stack[-1]
                    row_count[j] = row_count[prev_index] + heights[j] * (j - prev_index)
                else:
                    row_count[j] = heights[j] * (j + 1)
                
                stack.append(j)
            
            total += sum(row_count)
        
        return total
