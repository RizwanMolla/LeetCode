class Solution:
    def minLights(self, lights: list[int]) -> int:
        n = len(lights)

        diff = [0] * (n + 1)

        for i, v in enumerate(lights):
            if v > 0:
                l = max(0, i - v)
                r = min(n - 1, i + v)
                diff[l] += 1
                diff[r + 1] -= 1

        visible = [False] * n
        cur = 0
        for i in range(n):
            cur += diff[i]
            visible[i] = cur > 0

        ans = 0
        cover_until = -1

        for i in range(n):
            if not visible[i] and i > cover_until:
                ans += 1
                cover_until = i + 2

        return ans