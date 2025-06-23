class Solution:
    def kMirror(self, k: int, n: int) -> int:
        def is_palindrome(s: str) -> bool:
            return s == s[::-1]

        def to_base_k(num: int, base: int) -> str:
            res = []
            while num > 0:
                res.append(str(num % base))
                num //= base
            return ''.join(res[::-1])

        def generate_palindromes():
            # Odd and even length palindromes
            length = 1
            while True:
                # Odd length
                for half in range(10**(length - 1), 10**length):
                    s = str(half)
                    yield int(s + s[-2::-1])  # exclude last digit for odd-length
                # Even length
                for half in range(10**(length - 1), 10**length):
                    s = str(half)
                    yield int(s + s[::-1])
                length += 1

        count = 0
        total_sum = 0
        for num in generate_palindromes():
            base_k = to_base_k(num, k)
            if is_palindrome(base_k):
                total_sum += num
                count += 1
                if count == n:
                    break
        return total_sum
