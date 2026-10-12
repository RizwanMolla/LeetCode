class Solution:
    def threeFibonacciSum(self, n: int) -> bool:
        fib = [0, 1]
        while fib[-1] < n:
            fib.append(fib[-1] + fib[-2])
        for i in range(len(fib) - 2):
            if fib[i] + fib[i+1] + fib[i+2] == n:
                return True
        return False