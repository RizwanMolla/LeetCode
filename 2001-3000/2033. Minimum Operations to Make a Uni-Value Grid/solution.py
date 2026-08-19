class Solution:
    def minOperations(self, grid: list[list[int]], x: int) -> int:
        elements = []
        for row in grid:
            elements.extend(row)
        
        first = elements[0]
        for num in elements:
            if (num - first) % x != 0:
                return -1
        
        elements.sort()
        median = elements[len(elements) // 2]
        
        total_operations = 0
        for num in elements:
            total_operations += abs(num - median) // x
        
        return total_operations