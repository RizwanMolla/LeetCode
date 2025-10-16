class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        from collections import Counter
        cnt = Counter([num % value for num in nums])
        x = 0
        while True:
            if cnt[x % value] > 0:
                cnt[x % value] -= 1
                x += 1
            else:
                return x
