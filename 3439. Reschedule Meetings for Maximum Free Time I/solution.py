from typing import List

class Solution:
    def maxFreeTime(
        self, eventTime: int, k: int, startTime: List[int], endTime: List[int]
    ) -> int:
        freeIntervals = [startTime[0]]  #
        for i in range(1, len(endTime)):
            freeIntervals.append(startTime[i] - endTime[i - 1])
        freeIntervals.append(eventTime - endTime[-1])

        maxFree = 0
        currentWindowSum = 0

        for i, gap in enumerate(freeIntervals):
            currentWindowSum += gap
            if i >= k:
                maxFree = max(maxFree, currentWindowSum)
                currentWindowSum -= freeIntervals[i - k]

        return max(maxFree, currentWindowSum)
