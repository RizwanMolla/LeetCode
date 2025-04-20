from collections import Counter
import math

class Solution:
    def numRabbits(self, answers: list[int]) -> int:
        count = Counter(answers)
        total_rabbits = 0

        for x, freq in count.items():
            group_size = x + 1
            groups = math.ceil(freq / group_size)
            total_rabbits += groups * group_size

        return total_rabbits
