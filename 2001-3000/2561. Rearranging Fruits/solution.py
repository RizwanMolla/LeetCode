from collections import Counter
from typing import List

class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        count1 = Counter(basket1)
        count2 = Counter(basket2)

        total_count = count1 + count2

        for fruit, total in total_count.items():
            if total % 2 != 0:
                return -1

        surplus = []

        for fruit in total_count:
            diff = count1[fruit] - count2[fruit]
            if diff > 0:
                surplus.extend([fruit] * (diff // 2))
            elif diff < 0:
                surplus.extend([fruit] * (-(diff // 2)))

        surplus.sort()
        min_fruit = min(total_count.keys())

        cost = 0
        n = len(surplus) // 2
        for i in range(n):
            cost += min(surplus[i], 2 * min_fruit)

        return cost
