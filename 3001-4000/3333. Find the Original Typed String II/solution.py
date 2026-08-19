from itertools import accumulate

class Solution:
    def possibleStringCount(self, typed_string: str, min_length: int) -> int:
        MOD = 10**9 + 7
        run_diffs = []
        total_ways = 1
        current_run = 0

        for i, char in enumerate(typed_string):
            current_run += 1
            if i == len(typed_string) - 1 or char != typed_string[i + 1]:
                if current_run > 1:
                    if min_length > 0:
                        run_diffs.append(current_run - 1)
                    total_ways = total_ways * current_run % MOD
                current_run = 0
                min_length -= 1

        if min_length < 1:
            return total_ways

        run_count = len(run_diffs)
        dp = [[0] * min_length for _ in range(run_count + 1)]
        dp[0][0] = 1

        for i, max_remove in enumerate(run_diffs, 1):
            prefix_sum = list(accumulate(dp[i - 1], initial=0))
            for j in range(min_length):
                dp[i][j] = (prefix_sum[j + 1] - prefix_sum[j - min(max_remove, j)] + MOD) % MOD

        return (total_ways - sum(dp[run_count][j] for j in range(min_length))) % MOD
