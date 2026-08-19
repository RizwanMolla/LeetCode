class Solution(object):
    def shiftingLetters(self, s, shifts):
        n = len(s)
        shift = [0] * (n + 1)
        
        for start, end, direction in shifts:
            delta = 1 if direction == 1 else -1
            shift[start] += delta
            if end + 1 < n:
                shift[end + 1] -= delta

        for i in range(1, n):
            shift[i] += shift[i - 1]

        result = []
        for i in range(n):
            new_char = chr((ord(s[i]) - ord('a') + shift[i]) % 26 + ord('a'))
            result.append(new_char)

        return ''.join(result)


"""
Overview:
The solution uses a difference array to efficiently compute cumulative shifts across all indices. After applying the shifts, the result is constructed by wrapping each character within the alphabet, ensuring O(n + m) time complexity where n is the string length and m is the number of shifts.
"""