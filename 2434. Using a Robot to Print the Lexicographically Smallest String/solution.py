class Solution:
    def robotWithString(self, s: str) -> str:
        n = len(s)
        result = []
        stack = []
        
        # Precompute the minimum character from index i to the end
        min_suffix = [None] * n
        min_suffix[-1] = s[-1]
        for i in range(n - 2, -1, -1):
            min_suffix[i] = min(s[i], min_suffix[i + 1])
        
        for i in range(n):
            stack.append(s[i])
            # Keep popping from stack while the top is <= smallest char left in s
            while stack and (i == n - 1 or stack[-1] <= min_suffix[i + 1]):
                result.append(stack.pop())

        return ''.join(result)
