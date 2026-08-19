class Solution(object):
    def countPalindromicSubsequence(self, s):
        first = [-1] * 26
        last = [-1] * 26
        palindromes = set()

        for i, c in enumerate(s):
            idx = ord(c) - ord('a')
            if first[idx] == -1:
                first[idx] = i
            last[idx] = i

        for idx in range(26):
            if first[idx] != -1 and last[idx] != -1 and first[idx] < last[idx]:
                mid_chars = set(s[first[idx] + 1:last[idx]])
                for mid in mid_chars:
                    palindromes.add((chr(idx + ord('a')), mid, chr(idx + ord('a'))))

        return len(palindromes)
