class Solution(object):
    def canBeValid(self, s, locked):
        if len(s) % 2 != 0:
            return False
        
        open_balance, close_balance = 0, 0
        
        for i in range(len(s)):
            if locked[i] == '0' or s[i] == '(':
                open_balance += 1
            else:
                open_balance -= 1
            
            if open_balance < 0:
                return False
        
        for i in range(len(s) - 1, -1, -1):
            if locked[i] == '0' or s[i] == ')':
                close_balance += 1
            else:
                close_balance -= 1
            
            if close_balance < 0:
                return False
        
        return True
