class Solution:
    def generateValidStrings(self, n: int, k: int) -> list[str]:
        ans = []

        for mask in range(1 << n):
            s = format(mask, f"0{n}b")

            if "11" in s:
                continue

            cost = 0
            for i in range(n):
                if s[i] == '1':
                    cost += i

            if cost <= k:
                ans.append(s)

        return ans