class Solution:
    def clearStars(self, s: str) -> str:
        # Dictionary to store positions of each character
        char_positions = {}
        result = []
        
        for i, char in enumerate(s):
            if char == '*':
                # Find the lexicographically smallest character available
                smallest_char = None
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    if c in char_positions and char_positions[c]:
                        smallest_char = c
                        break
                
                # Remove the rightmost occurrence of the smallest character
                if smallest_char:
                    char_positions[smallest_char].pop()
                    if not char_positions[smallest_char]:
                        del char_positions[smallest_char]
            else:
                # Add character position to our tracking
                if char not in char_positions:
                    char_positions[char] = []
                char_positions[char].append(i)
        
        # Reconstruct the result string
        # Collect all remaining positions
        remaining_positions = []
        for positions in char_positions.values():
            remaining_positions.extend(positions)
        
        # Sort positions to maintain original order
        remaining_positions.sort()
        
        # Build result string
        result = []
        for pos in remaining_positions:
            result.append(s[pos])
        
        return ''.join(result)