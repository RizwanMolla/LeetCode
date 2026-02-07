class Solution:
    def minimumDeletions(self, s: str) -> int:
        bCount = 0   
        ans = 0      
        
        for ch in s:
            if ch == 'b':
                bCount += 1
            else:  # ch == 'a'
                ans = min(ans + 1, bCount)
        
        return ans
