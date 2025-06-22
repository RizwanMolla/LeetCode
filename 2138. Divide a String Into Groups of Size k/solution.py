class Solution:
    def divideString(self, s: str, k: int, fill: str) -> list[str]:
        result = []
        
        for i in range(0, len(s), k):
            group = s[i:i+k]
            
            if len(group) < k:
                group += fill * (k - len(group))
            
            result.append(group)
        
        return result