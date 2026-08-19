class Solution:
    def punishmentNumber(self, n: int) -> int:
        def canPartition(s, target, index, current_sum):
            if index == len(s):  
                return current_sum == target

            num = 0
            for j in range(index, len(s)):  
                num = num * 10 + int(s[j])  
                if num + current_sum > target:  
                    break  
                if canPartition(s, target, j + 1, current_sum + num):
                    return True
            return False
        
        total_punishment = 0
        for i in range(1, n + 1):
            square_str = str(i * i)
            if canPartition(square_str, i, 0, 0):
                total_punishment += i * i  
        
        return total_punishment