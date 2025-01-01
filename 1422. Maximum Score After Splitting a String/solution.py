class Solution(object):
    def maxScore(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_score = 0
        ones_count = s.count('1')
        zeros_count = 0
        
        for i in range(len(s) - 1):
            if s[i] == '0':
                zeros_count += 1
            else:
                ones_count -= 1
            max_score = max(max_score, zeros_count + ones_count)
        
        return max_score
    

"""
Explanation:
The solution uses a single pass through the string to calculate the maximum score after splitting. It maintains the count of zeros in the left substring and the count of ones in the right substring as it iterates. The score for each possible split is calculated and the maximum score is tracked. This approach achieves O(n) time complexity and O(1) space complexity.
"""