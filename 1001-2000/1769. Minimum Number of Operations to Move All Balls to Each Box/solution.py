class Solution(object):
    def minOperations(self, boxes):
        n = len(boxes)
        answer = [0] * n
        
        count = 0
        moves = 0
        for i in range(n):
            answer[i] += moves
            count += int(boxes[i])
            moves += count
            
        count = 0
        moves = 0
        for i in range(n - 1, -1, -1):
            answer[i] += moves
            count += int(boxes[i])
            moves += count
        
        return answer

"""
Overview:
The algorithm efficiently calculates the minimum number of operations using two passes: one from left to right and another from right to left. It keeps track of the cumulative number of balls and their movement cost in each direction, ensuring O(n) time complexity for the solution.
"""