class Solution:
    def limitOccurrences(self, nums: list[int], k: int) -> list[int]:
        res = []
        count = 0
        prev = None

        for num in nums:
            if num != prev:
                prev = num
                count = 1
            else:
                count += 1

            if count <= k:
                res.append(num)

        return res