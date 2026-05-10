class Solution:
    def minFlips(self, s: str) -> int:

        n = len(s)
        if n <= 1:
            return 0
        
        total_ones = s.count('1')
        total_zeros = n - total_ones
        
        c_a = total_ones
        c_b = total_zeros
        c_c = max(0, total_ones - 1)

        inner_ones = total_ones - (s[0] == '1') - (s[-1] == '1')
        c_d = (s[0] != '1') + (s[-1] != '1') + inner_ones
        
        return min(c_a, c_b, c_c, c_d)