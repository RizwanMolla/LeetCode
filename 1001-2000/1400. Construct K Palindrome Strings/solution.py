class Solution(object):
    def canConstruct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """
        if len(s) < k:
            return False
        freq = {}
        for char in s:
            freq[char] = freq.get(char, 0) + 1
        odd_count = sum(1 for count in freq.values() if count % 2 != 0)
        return odd_count <= k
