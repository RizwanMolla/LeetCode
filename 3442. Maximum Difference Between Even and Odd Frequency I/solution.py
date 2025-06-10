from collections import Counter

class Solution:
    def maxDifference(self, s: str) -> int:
        freq = Counter(s)  # Count frequencies of each character
        
        odd_freqs = [count for count in freq.values() if count % 2 == 1]
        even_freqs = [count for count in freq.values() if count % 2 == 0]
        
        # We are guaranteed at least one odd and one even frequency
        max_odd = max(odd_freqs)
        min_even = min(even_freqs)
        
        return max_odd - min_even
