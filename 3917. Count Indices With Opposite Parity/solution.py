class Solution:
    def countOppositeParity(self, nums: list[int]) -> list[int]:
        n = len(nums)
        ans = [0] * n
    
        even_cnt = 0
        odd_cnt = 0
    
        for i in range(n - 1, -1, -1):
            if nums[i] % 2 == 0:
                ans[i] = odd_cnt
                even_cnt += 1
            else:
                ans[i] = even_cnt
                odd_cnt += 1
    
        return ans