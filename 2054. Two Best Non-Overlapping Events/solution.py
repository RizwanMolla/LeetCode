class Solution:
    def maxTwoEvents(self, events: list[list[int]]) -> int:
        line_sweep = []
        for start, end, val in events:
            line_sweep.append([start, 1, val])
            line_sweep.append([end + 1, -1, val])
        line_sweep.sort()

        max_val = 0
        max_seen = 0
        for point, status, val in line_sweep:
            if status == 1:
                max_val = max(max_val, max_seen + val)
            elif status == -1:
                max_seen = max(max_seen, val)
        return max_val