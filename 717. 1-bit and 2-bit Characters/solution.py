class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        i = 0
        n = len(bits)
        
        while i < n - 1:     # Stop before the last element
            if bits[i] == 1:
                i += 2       # two-bit character
            else:
                i += 1       # one-bit character
        
        # If we ended exactly at the last index, it's a one-bit character
        return i == n - 1
