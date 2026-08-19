from typing import List

class BIT:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 2)

    def update(self, i, delta):
        i += 1
        while i <= self.n + 1:
            self.tree[i] += delta
            i += i & -i

    def query(self, i):
        i += 1
        res = 0
        while i > 0:
            res += self.tree[i]
            i -= i & -i
        return res

class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        pos = [0] * n
        for i in range(n):
            pos[nums2[i]] = i

        mapped = [pos[num] for num in nums1]

        left_BIT = BIT(n)
        left_count = [0] * n

        for i in range(n):
            left_count[i] = left_BIT.query(mapped[i] - 1)
            left_BIT.update(mapped[i], 1)

        right_BIT = BIT(n)
        right_count = [0] * n

        for i in reversed(range(n)):
            right_count[i] = right_BIT.query(n - 1) - right_BIT.query(mapped[i])
            right_BIT.update(mapped[i], 1)

        result = 0
        for i in range(n):
            result += left_count[i] * right_count[i]

        return result
