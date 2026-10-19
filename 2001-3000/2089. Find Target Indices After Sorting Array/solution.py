class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        nums.sort()
        res=[]
        for i, n in enumerate(nums):
            if n == target:
                res.append(i)

        return res

