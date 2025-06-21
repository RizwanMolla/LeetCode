from collections import Counter

class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        freq = list(Counter(word).values())
        freq.sort()
        n = len(freq)
        min_deletions = float('inf')

        for i in range(n):

            deletions = 0
            for j in range(i):
                deletions += freq[j]
            for j in range(i + 1, n):
                if freq[j] > freq[i] + k:
                    deletions += freq[j] - (freq[i] + k)
            min_deletions = min(min_deletions, deletions)

        return min_deletions
