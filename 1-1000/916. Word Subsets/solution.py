class Solution(object):
    def wordSubsets(self, words1, words2):
        from collections import Counter

        def merge_counts(words):
            max_count = Counter()
            for word in words:
                word_count = Counter(word)
                for char in word_count:
                    max_count[char] = max(max_count[char], word_count[char])
            return max_count

        b_max_count = merge_counts(words2)
        result = []

        for word in words1:
            word_count = Counter(word)
            if all(word_count[char] >= b_max_count[char] for char in b_max_count):
                result.append(word)

        return result
