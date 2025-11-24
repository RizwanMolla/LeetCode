class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        ans = []
        curr = 0
        for x in nums:
            curr = (curr * 2 + x) % 5
            ans.append(curr == 0)
        return ans