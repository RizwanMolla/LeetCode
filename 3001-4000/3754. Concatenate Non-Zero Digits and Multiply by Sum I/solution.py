class Solution:
    def sumAndMultiply(self, n: int) -> int:
        x = "".join(ch for ch in str(n) if ch != "0")
        if not x:
            x = "0"

        totalSum = sum(int(ch) for ch in x)
        return int(x) * totalSum