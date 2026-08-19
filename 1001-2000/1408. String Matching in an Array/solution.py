class Solution(object):
    def stringMatching(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        result = []
        for i, word in enumerate(words):
            for j, other_word in enumerate(words):
                if i != j and word in other_word:
                    result.append(word)
                    break
        return result
