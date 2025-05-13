class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        MOD = 10**9 + 7

        char_count = {}
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1
        
        for _ in range(t):
            new_count = {}
            for char, count in char_count.items():
                if char == 'z':
                    new_count['a'] = (new_count.get('a', 0) + count) % MOD
                    new_count['b'] = (new_count.get('b', 0) + count) % MOD
                else:
                    next_char = chr(ord(char) + 1)
                    new_count[next_char] = (new_count.get(next_char, 0) + count) % MOD
            
            char_count = new_count
        
        total_length = sum(char_count.values()) % MOD
        
        return total_length