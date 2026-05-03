class Solution:
    def sumOfPrimesInRange(self, n: int) -> int:

        rNum = int(str(n)[::-1])
        
        start = min(n, rNum)
        end = max(n, rNum)
        
        def is_prime(x):
            if x < 2:
                return False
            for i in range(2, int(x ** 0.5) + 1):
                if x % i == 0:
                    return False
            return True
        
        total = 0
        
        for num in range(start, end + 1):
            if is_prime(num):
                total += num
        
        return total