from collections import defaultdict

class Solution:
    def tupleSameProduct(self, nums: list[int]) -> int:
        product_count = defaultdict(int)
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                product = nums[i] * nums[j]
                product_count[product] += 1
        result = 0
        for count in product_count.values():
            if count >= 2:
                result += count * (count - 1) * 4
        return result