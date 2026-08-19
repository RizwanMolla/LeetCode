class Solution:
    def findEvenNumbers(self, digits: list[int]) -> list[int]:
        n = len(digits)
        result = set()  # Using a set to store unique numbers
        
        # Generate all possible 3-digit numbers
        for i in range(n):
            # Skip if the first digit is 0 (to avoid leading zeros)
            if digits[i] == 0:
                continue
                
            for j in range(n):
                # Skip using the same position twice
                if j == i:
                    continue
                    
                for k in range(n):
                    # Skip using the same position twice
                    if k == i or k == j:
                        continue
                    
                    # Calculate the number
                    num = digits[i] * 100 + digits[j] * 10 + digits[k]
                    
                    # Check if the number is even (last digit must be even)
                    if digits[k] % 2 == 0:
                        result.add(num)
        
        # Convert to list and sort
        return sorted(list(result))