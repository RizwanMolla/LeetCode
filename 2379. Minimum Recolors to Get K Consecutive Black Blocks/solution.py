class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        min_operations = float('inf')
        white_count = 0
        
        for i in range(k):
            if blocks[i] == 'W':
                white_count += 1
        
        min_operations = white_count
        
        for i in range(k, len(blocks)):
            if blocks[i] == 'W':
                white_count += 1
            if blocks[i - k] == 'W':
                white_count -= 1
            
            min_operations = min(min_operations, white_count)
        
        return min_operations
