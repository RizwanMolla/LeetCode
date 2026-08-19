from collections import Counter

class Solution:
    def longestPalindrome(self, words: list[str]) -> int:
        count = Counter(words)
        length = 0
        used_middle = False

        for word in list(count.keys()):
            rev = word[::-1]
            if word == rev:
                pairs = count[word] // 2
                length += pairs * 4
                count[word] -= pairs * 2
            else:
                if rev in count:
                    pairs = min(count[word], count[rev])
                    length += pairs * 4
                    count[word] -= pairs
                    count[rev] -= pairs
        for word in count:
            if word[0] == word[1] and count[word] > 0:
                length += 2
                break

        return length
