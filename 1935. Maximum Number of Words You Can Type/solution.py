class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        broken_set = set(brokenLetters)  # Use a set for O(1) lookup
        count = 0
        
        for word in text.split():
            if all(char not in broken_set for char in word):
                count += 1
                
        return count
