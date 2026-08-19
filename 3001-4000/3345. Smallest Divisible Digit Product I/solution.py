class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        def check(n: int) -> bool:
            product = 1
            while n > 0:
                product *= n % 10
                n //= 10
                if product == 0:
                    break
            return product % t == 0

        while not check(n):
            n += 1
        return n