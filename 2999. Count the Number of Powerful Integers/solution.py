from functools import cache

class Solution:
    def numberOfPowerfulInt(self, low: int, high: int, maxDigit: int, suffix: str) -> int:
        @cache
        def count(pos: int, tight: bool) -> int:
            if len(curr) < suffixLen:
                return 0
            if len(curr) - pos == suffixLen:
                return int(suffix <= curr[pos:]) if tight else 1
            
            upper = int(curr[pos]) if tight else 9
            upper = min(upper, maxDigit)
            total = 0

            for digit in range(upper + 1):
                total += count(pos + 1, tight and digit == int(curr[pos]))
            
            return total

        suffixLen = len(suffix)

        curr = str(low - 1)
        left = count(0, True)
        count.cache_clear()

        curr = str(high)
        right = count(0, True)

        return right - left
