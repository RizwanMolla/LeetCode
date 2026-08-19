class Solution:
    def numberOfPairs(self, points: list[list[int]]) -> int:
        n = len(points)
        count = 0
        
        # Sort points by x-coordinate, then y-coordinate
        points.sort()
        
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                
                x1, y1 = points[i]
                x2, y2 = points[j]
                
                # Check for "upper left" condition
                if x1 <= x2 and y1 >= y2:
                    is_empty = True
                    # Check for any other point inside the rectangle
                    for k in range(n):
                        if k == i or k == j:
                            continue
                        
                        x3, y3 = points[k]
                        
                        # Check if a point is inside the rectangle (including border)
                        if x1 <= x3 <= x2 and y2 <= y3 <= y1:
                            is_empty = False
                            break
                    
                    if is_empty:
                        count += 1
                        
        return count