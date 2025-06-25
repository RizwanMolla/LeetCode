from bisect import bisect_right, bisect_left
from typing import List

class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        def countLessEqual(product_limit: int) -> int:
            count = 0
            length_nums2 = len(nums2)
            for num1 in nums1:
                if num1 > 0:
                    count += bisect_right(nums2, product_limit / num1)
                elif num1 < 0:
                    count += length_nums2 - bisect_left(nums2, product_limit / num1)
                else:
                    count += length_nums2 * int(product_limit >= 0)
            return count

        max_possible_product = max(abs(nums1[0]), abs(nums1[-1])) * max(abs(nums2[0]), abs(nums2[-1]))
        return bisect_left(range(-max_possible_product, max_possible_product + 1), k, key=countLessEqual) - max_possible_product
