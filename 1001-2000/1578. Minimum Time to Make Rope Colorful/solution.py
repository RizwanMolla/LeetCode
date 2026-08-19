class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        total_time = 0
        
        for i in range(1, len(colors)):
            if colors[i] == colors[i - 1]:
                # remove the one with smaller time
                total_time += min(neededTime[i], neededTime[i - 1])
                # keep the max for next comparison
                neededTime[i] = max(neededTime[i], neededTime[i - 1])
        
        return total_time
