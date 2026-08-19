from functools import cache
from bisect import bisect_right
from typing import List

class Solution:
    def maxValue(self, events: List[List[int]], maxEvents: int) -> int:
        @cache
        def dfs(currentIndex: int, remainingEvents: int) -> int:
            if currentIndex >= len(events):
                return 0

            startTime, endTime, value = events[currentIndex]

            maxValueWithoutCurrent = dfs(currentIndex + 1, remainingEvents)

            maxValueWithCurrent = 0
            if remainingEvents:
                nextIndex = bisect_right(events, endTime, lo=currentIndex + 1, key=lambda x: x[0])
                maxValueWithCurrent = dfs(nextIndex, remainingEvents - 1) + value

            return max(maxValueWithoutCurrent, maxValueWithCurrent)

        events.sort()
        return dfs(0, maxEvents)
