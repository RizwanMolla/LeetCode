class Solution:
    def minMaxDifference(self, num: int) -> int:
        """
        Find the maximum difference by remapping exactly one digit.
        
        Args:
            num: int - the input number
            
        Returns:
            int - difference between maximum and minimum possible values
        """
        num_str = str(num)
        
        # Calculate maximum value
        max_val = self.getMaxValue(num_str)
        
        # Calculate minimum value
        min_val = self.getMinValue(num_str)
        
        return max_val - min_val
    
    def getMaxValue(self, num_str):
        """
        Get maximum value by replacing first non-9 digit with 9.
        """
        # Find first digit that is not 9
        for digit in num_str:
            if digit != '9':
                # Replace all occurrences of this digit with 9
                return int(num_str.replace(digit, '9'))
        
        # If all digits are 9, return the original number
        return int(num_str)
    
    def getMinValue(self, num_str):
        """
        Get minimum value by strategic digit replacement.
        """
        min_val = int(num_str)
        
        # Try replacing each unique digit with 0
        for digit in set(num_str):
            if digit != '0':
                candidate = int(num_str.replace(digit, '0'))
                min_val = min(min_val, candidate)
        
        return min_val