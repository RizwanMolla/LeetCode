from bisect import bisect_left, bisect_right
from typing import List


class RangeMaxQuery:
    def __init__(self, values: List[int]):
        self.table = [values[:]]
        length = len(values)
        step = 1

        while step * 2 <= length + 1:
            prev = self.table[-1]
            current = []

            for idx in range(length - 2 * step + 1):
                current.append(max(prev[idx], prev[idx + step]))

            self.table.append(current)
            step <<= 1

    def get_max(self, left: int, right: int) -> int:
        if left > right:
            return 0

        power = (right - left + 1).bit_length() - 1
        size = 1 << power

        return max(
            self.table[power][left],
            self.table[power][right - size + 1],
        )


class Solution:
    def maxActiveSectionsAfterTrade(
        self,
        binaryString: str,
        queries: List[List[int]]
    ) -> List[int]:

        totalActive = binaryString.count("1")
        n = len(binaryString)

        zeroLengths = []
        zeroStart = []
        zeroEnd = []

        pointer = 0

        while pointer < n:
            segmentStart = pointer
            currentChar = binaryString[pointer]

            while pointer < n and binaryString[pointer] == currentChar:
                pointer += 1

            if currentChar == "0":
                zeroLengths.append(pointer - segmentStart)
                zeroStart.append(segmentStart)
                zeroEnd.append(pointer - 1)

        zeroSegmentCount = len(zeroLengths)

        if zeroSegmentCount < 2:
            return [totalActive] * len(queries)

        adjacentMerge = [
            zeroLengths[i] + zeroLengths[i + 1]
            for i in range(zeroSegmentCount - 1)
        ]

        rmq = RangeMaxQuery(adjacentMerge)

        answer = []

        for leftBound, rightBound in queries:

            firstSegment = bisect_left(zeroEnd, leftBound)
            lastSegment = bisect_right(zeroStart, rightBound) - 1

            if (
                firstSegment >= zeroSegmentCount
                or lastSegment < 0
                or firstSegment >= lastSegment
            ):
                answer.append(totalActive)
                continue

            leftContribution = (
                zeroEnd[firstSegment]
                - max(zeroStart[firstSegment], leftBound)
                + 1
            )

            rightContribution = (
                min(zeroEnd[lastSegment], rightBound)
                - zeroStart[lastSegment]
                + 1
            )

            if firstSegment + 1 == lastSegment:
                answer.append(totalActive + leftContribution + rightContribution)
                continue

            candidateLeft = (
                leftContribution + zeroLengths[firstSegment + 1]
            )

            candidateRight = (
                zeroLengths[lastSegment - 1] + rightContribution
            )

            candidateMiddle = rmq.get_max(
                firstSegment + 1,
                lastSegment - 2,
            )

            bestIncrease = max(
                candidateLeft,
                candidateRight,
                candidateMiddle,
            )

            answer.append(totalActive + bestIncrease)

        return answer