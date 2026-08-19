class Solution:
    def maxCount(self, b: list[int], n: int, m: int) -> int:
        s = set(b)
        c, total = 0, 0
        
        for x in range(1, n + 1):
            if x not in s:
                total += x
                if total > m:
                    break
                c += 1
                
        return c
