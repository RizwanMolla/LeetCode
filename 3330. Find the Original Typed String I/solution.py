class Solution:
    def possibleStringCount(self, word: str) -> int:
        n = len(word)
        groups = []
        i = 0

        # Group consecutive same characters
        while i < n:
            j = i
            while j < n and word[j] == word[i]:
                j += 1
            groups.append((word[i], j - i))
            i = j

        total = 1  # Start with the original word
        for i, (char, count) in enumerate(groups):
            if count > 1:
                total += count - 1  # We can reduce this group by 1 to (count - 1) characters

        return total
