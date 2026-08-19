from collections import Counter

class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        def count_valid_substrings(limit: int) -> int:
            vowel_freq = Counter()
            total_count = left = consonant_count = 0
            
            for char in word:
                if char in "aeiou":
                    vowel_freq[char] += 1
                else:
                    consonant_count += 1

                while consonant_count >= limit and len(vowel_freq) == 5:
                    removed_char = word[left]
                    if removed_char in "aeiou":
                        vowel_freq[removed_char] -= 1
                        if vowel_freq[removed_char] == 0:
                            del vowel_freq[removed_char]
                    else:
                        consonant_count -= 1
                    left += 1
                
                total_count += left
            
            return total_count

        return count_valid_substrings(k) - count_valid_substrings(k + 1)
