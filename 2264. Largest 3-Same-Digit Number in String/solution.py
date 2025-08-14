class Solution:
    def largestGoodInteger(self, num: str) -> str:
        max_good = ""
        
        for i in range(len(num) - 2):
            sub = num[i:i+3]
            if len(set(sub)) == 1:  # All characters same
                if sub > max_good:
                    max_good = sub
        
        return max_good
