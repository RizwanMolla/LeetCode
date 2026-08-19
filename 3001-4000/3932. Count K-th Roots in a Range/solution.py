class Solution:
    def countKthRoots(self, l: int, r: int, k: int) -> int:
        def kth_root_floor(n):
            lo, hi = 0, 10**9

            while lo <= hi:
                mid = (lo + hi) // 2

                if mid ** k <= n:
                    lo = mid + 1
                else:
                    hi = mid - 1

            return hi

        return kth_root_floor(r) - kth_root_floor(l - 1)