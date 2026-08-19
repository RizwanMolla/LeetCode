class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def remove_substring(s: str, a: str, b: str, val: int) -> str:
        # def remove_substring(s: str, a: str, b: str, val: int) -> (str, int):
            stack = []
            score = 0
            for char in s:
                if stack and stack[-1] == a and char == b:
                    stack.pop()
                    score += val
                else:
                    stack.append(char)
            return ''.join(stack), score
        
        total = 0
        if x > y:
            s, score1 = remove_substring(s, 'a', 'b', x)
            _, score2 = remove_substring(s, 'b', 'a', y)
        else:
            s, score1 = remove_substring(s, 'b', 'a', y)
            _, score2 = remove_substring(s, 'a', 'b', x)

        return score1 + score2
