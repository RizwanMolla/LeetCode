class Solution:
    def maximumSum(self, nums: List[int], m: int, l: int, r: int) -> int:
        n = len(nums)

        pre = [0] * (n + 1)
        for i in range(n):
            pre[i + 1] = pre[i] + nums[i]

        neg = float('-inf')

        from collections import deque

        def dp(arr, first):
            cur = [neg] * n

            pm = [neg] * (n + 1)
            pm[0] = 0 if first else neg

            for i in range(1, n + 1):
                pm[i] = pm[i - 1]
                if arr[i - 1] != neg:
                    pm[i] = max(pm[i], arr[i - 1])

            dq = deque()

            for i in range(n):
                s = i - l + 1

                if 0 <= s <= n and pm[s] != neg:
                    v = pm[s] - pre[s]

                    while dq and (pm[dq[-1]] - pre[dq[-1]]) <= v:
                        dq.pop()
                    dq.append(s)

                while dq and dq[0] < i - r + 1:
                    dq.popleft()

                if dq:
                    cur[i] = pre[i + 1] + pm[dq[0]] - pre[dq[0]]

            return cur

        prev = dp([neg] * n, True)

        ans = max(x for x in prev if x != neg)

        for _ in range(2, m + 1):
            cur = dp(prev, False)

            for x in cur:
                if x != neg:
                    ans = max(ans, x)

            prev = cur

        return ans