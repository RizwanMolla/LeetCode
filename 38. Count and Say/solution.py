class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        
        prev = "1"
        for _ in range(2, n + 1):
            result = ""
            count = 1
            for j in range(1, len(prev)):
                if prev[j] == prev[j - 1]:
                    count += 1
                else:
                    result += str(count) + prev[j - 1]
                    count = 1
            result += str(count) + prev[-1]  # append the last group
            prev = result
        
        return prev
