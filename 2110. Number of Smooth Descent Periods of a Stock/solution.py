class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        ans = 1
        curr = 1
        
        for i in range(1, len(prices)):
            if prices[i] == prices[i - 1] - 1:
                curr += 1
            else:
                curr = 1
            ans += curr
        
        return ans
