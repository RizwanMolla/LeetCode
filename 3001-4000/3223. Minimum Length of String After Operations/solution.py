import collections

class Solution:
    def minimumLength(self, s: str) -> int:
        char_count = collections.Counter(s)
        result = 0
        for char in char_count.keys():
            result += 2 - (char_count[char] % 2)
        return result