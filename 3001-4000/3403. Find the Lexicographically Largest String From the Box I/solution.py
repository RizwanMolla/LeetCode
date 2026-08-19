class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends == 1:
            return word
        
        max_suffix = self.findMaxSuffix(word)
        max_length = len(word) - numFriends + 1
        return max_suffix[:max_length]

    def findMaxSuffix(self, text: str) -> str:
        left, right, offset = 0, 1, 0
        n = len(text)
        
        while right + offset < n:
            if text[left + offset] == text[right + offset]:
                offset += 1
            elif text[left + offset] < text[right + offset]:
                left = max(left + offset + 1, right)
                right = left + 1
                offset = 0
            else:
                right = right + offset + 1
                offset = 0
        
        return text[left:]
