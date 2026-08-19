class Solution:
    def minGenerations(self, points: List[List[int]], target: List[int]) -> int:
        target = tuple(target)

        seen = set(tuple(p) for p in points)

        if target in seen:
            return 0

        gen = 0

        while True:
            gen += 1

            current = list(seen)
            newPoints = set()

            for i in range(len(current)):
                x1, y1, z1 = current[i]

                for j in range(i + 1, len(current)):
                    x2, y2, z2 = current[j]

                    if current[i] == current[j]:
                        continue

                    mid = (
                        (x1 + x2) // 2,
                        (y1 + y2) // 2,
                        (z1 + z2) // 2
                    )

                    if mid not in seen:
                        newPoints.add(mid)

            if not newPoints:
                return -1

            if target in newPoints:
                return gen

            seen |= newPoints