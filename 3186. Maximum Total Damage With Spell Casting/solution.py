from bisect import bisect_left
from collections import Counter

class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        count = Counter(power)
        damages = sorted(count.keys())
        
        total = [d * count[d] for d in damages]
        n = len(damages)
        dp = [0] * n
        
        dp[0] = total[0]
        
        for i in range(1, n):
            # Binary search to find last index j where damages[j] < damages[i] - 2
            j = bisect_left(damages, damages[i] - 2) - 1
            take = total[i] + (dp[j] if j >= 0 else 0)
            not_take = dp[i-1]
            dp[i] = max(take, not_take)
        
        return dp[-1]
