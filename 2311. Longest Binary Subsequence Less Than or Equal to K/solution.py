class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        count = 0
        value = 0
        power = 1
        
        for ch in reversed(s):
            if ch == '0':
                count += 1
            else:
                if power <= k - value:
                    value += power
                    count += 1
            power <<= 1
            if power > k:
                break

        count += s[:len(s) - count].count('0')
        
        return count
