class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        freq = {}
        
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1
        
        max_vowel = 0
        max_consonant = 0
    
        for ch, count in freq.items():
            if ch in vowels:
                max_vowel = max(max_vowel, count)
            else:
                max_consonant = max(max_consonant, count)
        
        return max_vowel + max_consonant
