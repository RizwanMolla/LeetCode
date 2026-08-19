class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums.sort()
        ans = []
        for x, y in pairwise(nums):
            ans.extend(range(x + 1, y))
        return ans