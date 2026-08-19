class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        from collections import defaultdict

        n = len(nums)

        BASE = 911382323
        MOD = (1 << 61) - 1

        # powers
        power = [1] * (n + 1)
        for i in range(n):
            power[i + 1] = (power[i] * BASE) % MOD

        # prefix hash
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = (pref[i] * BASE + nums[i] + 7) % MOD

        def get_hash(l, r):
            return (pref[r] - pref[l] * power[r - l]) % MOD

        def ok(L):
            freq = defaultdict(int)

            for i in range(n - L + 1):
                h = get_hash(i, i + L)
                freq[h] += 1

            for v in freq.values():
                if v == 1:
                    return True

            return False

        lo, hi = 1, n
        ans = n

        while lo <= hi:
            mid = (lo + hi) // 2

            if ok(mid):
                ans = mid
                hi = mid - 1
            else:
                lo = mid + 1

        return ans