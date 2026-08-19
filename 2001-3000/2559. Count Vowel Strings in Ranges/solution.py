class Solution(object):
    def vowelStrings(self, words, queries):
        """
        :type words: List[str]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        vowels = {'a', 'e', 'i', 'o', 'u'}
        prefix_count = [0] * (len(words) + 1)
        
        for i, word in enumerate(words):
            if word[0] in vowels and word[-1] in vowels:
                prefix_count[i + 1] = prefix_count[i] + 1
            else:
                prefix_count[i + 1] = prefix_count[i]
        
        result = []
        for li, ri in queries:
            result.append(prefix_count[ri + 1] - prefix_count[li])
        
        return result


"""
Explanation:
The solution preprocesses the input by building a prefix sum array, where each entry contains the cumulative count of strings starting and ending with a vowel up to that index. For each query, the result is computed in O(1) time by subtracting the prefix sum at the start of the range from the prefix sum at the end of the range. This ensures efficient handling of large inputs with an O(n+q) time complexity, where n is the length of the words array and q is the number of queries.
"""
