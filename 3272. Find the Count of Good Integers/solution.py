from math import factorial
from collections import Counter

class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        factorials = [factorial(i) for i in range(n + 1)]
        good_count = 0
        seen_digit_signatures = set()
        
        half_start = 10 ** ((n - 1) // 2)
        half_end = half_start * 10

        for half in range(half_start, half_end):
            half_str = str(half)
            full_palindrome = half_str + half_str[::-1][n % 2:]

            if int(full_palindrome) % k != 0:
                continue

            digit_signature = ''.join(sorted(full_palindrome))

            if digit_signature in seen_digit_signatures:
                continue
            seen_digit_signatures.add(digit_signature)

            digit_freq = Counter(digit_signature)
            permutations = (n - digit_freq['0']) * factorials[n - 1]

            for count in digit_freq.values():
                permutations //= factorials[count]

            good_count += permutations

        return good_count
