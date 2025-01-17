from typing import List

class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        n = len(derived)

        def is_valid(start):
            current = start
            for i in range(n):
                next_val = current ^ derived[i]
                current = next_val
            return current == start

        return is_valid(0) or is_valid(1)
