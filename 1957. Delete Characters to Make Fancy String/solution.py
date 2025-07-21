class Solution:
    def makeFancyString(self, s: str) -> str:
        result = []
        for c in s:
            n = len(result)
            if n < 2 or not (result[-1] == c and result[-2] == c):
                result.append(c)
        return ''.join(result)
