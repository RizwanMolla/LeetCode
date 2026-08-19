class Solution(object):
    def countPrefixSuffixPairs(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        def isPrefixAndSuffix(prefix, word):
            return word.startswith(prefix) and word.endswith(prefix)
        
        count = 0
        n = len(words)
        
        for i in range(n):
            for j in range(i + 1, n):
                if isPrefixAndSuffix(words[i], words[j]):
                    count += 1
        
        return count
