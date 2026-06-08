class Solution:
    def sumOfGoodIntegers(self, n: int, k: int) -> int:
        left = max(1, n - k)
        right = n + k

        ans = 0
        for x in range(left, right + 1):
            if (n & x) == 0:
                ans += x

        return ans