class Solution:
    def checkString(self, s: str) -> bool:
        sorted_string = ''.join(sorted(s))
        return s == sorted_string