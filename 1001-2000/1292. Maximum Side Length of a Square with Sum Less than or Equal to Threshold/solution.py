class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        m, n = len(mat), len(mat[0])
        
        pre = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                pre[i][j] = (
                    mat[i - 1][j - 1]
                    + pre[i - 1][j]
                    + pre[i][j - 1]
                    - pre[i - 1][j - 1]
                )
        
        def can(k):
            for i in range(k, m + 1):
                for j in range(k, n + 1):
                    total = (
                        pre[i][j]
                        - pre[i - k][j]
                        - pre[i][j - k]
                        + pre[i - k][j - k]
                    )
                    if total <= threshold:
                        return True
            return False
        
        left, right = 0, min(m, n)
        ans = 0
        while left <= right:
            mid = (left + right) // 2
            if can(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        
        return ans
