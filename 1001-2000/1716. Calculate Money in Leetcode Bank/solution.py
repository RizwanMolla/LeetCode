class Solution:
    def totalMoney(self, n: int) -> int:
        week = n // 7
        day = n % 7
        
        total = (28 * week) + (7 * week * (week - 1)) // 2
        
        total += day * (week + 1) + (day * (day - 1)) // 2
        
        return total
