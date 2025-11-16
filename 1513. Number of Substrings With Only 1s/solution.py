class Solution:
    def numSub(self, s: str) -> int:
        MOD = 10**9 + 7
        count = 0      # count of consecutive 1s
        ans = 0

        for ch in s:
            if ch == '1':
                count += 1
            else:
                ans = (ans + count * (count + 1) // 2) % MOD
                count = 0

        # Add last segment if the string ends with '1's
        ans = (ans + count * (count + 1) // 2) % MOD

        return ans
