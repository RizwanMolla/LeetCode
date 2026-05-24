class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        inf = float('inf')
    
        def s(a):
            p = next(i for i in range(n) if a[i] == 0)
    
            if all(a[(p + i) % n] == i for i in range(n)):
                return p
    
            return inf
    
        def r(a):
            p = next(i for i in range(n) if a[i] == n - 1)
    
            if all(a[(p + i) % n] == n - 1 - i for i in range(n)):
                return p
    
            return inf
    
        rev = nums[::-1]
    
        ans = inf
    
        ans = min(ans, s(nums))
        ans = min(ans, 1 + s(rev))
        ans = min(ans, r(nums) + 1)
        ans = min(ans, 2 + r(rev))
    
        return ans if ans != inf else -1