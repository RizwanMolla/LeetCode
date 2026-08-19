from typing import List

class Solution:
    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        n = len(startTime)
        durations = [end - start for start, end in zip(startTime, endTime)]
        maxLeftGap = [0] * n
        maxRightGap = [0] * n

        maxLeftGap[0] = startTime[0]
        for i in range(1, n):
            maxLeftGap[i] = max(maxLeftGap[i - 1], startTime[i] - endTime[i - 1])

        maxRightGap[n - 1] = eventTime - endTime[-1]
        for i in range(n - 2, -1, -1):
            maxRightGap[i] = max(maxRightGap[i + 1], startTime[i + 1] - endTime[i])

        res = 0
        for i in range(n):
            left = startTime[i] - endTime[i - 1] if i > 0 else startTime[0]
            right = startTime[i + 1] - endTime[i] if i < n - 1 else eventTime - endTime[-1]
            movable = 0
            if (i > 0 and maxLeftGap[i - 1] >= durations[i]) or (i < n - 1 and maxRightGap[i + 1] >= durations[i]):
                movable = durations[i]
            res = max(res, left + movable + right)

        return res
