from collections import Counter

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        char_count = Counter()
        left = 0
        total_substrings = 0
        
        for right, char in enumerate(s):
            char_count[char] += 1
            
            while len(char_count) == 3:
                char_count[s[left]] -= 1
                if char_count[s[left]] == 0:
                    del char_count[s[left]]
                left += 1
            
            total_substrings += left

        return total_substrings
