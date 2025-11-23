class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        total = sum(nums)

        # Lists to store smallest numbers with remainder 1 and 2
        rem1 = []
        rem2 = []

        for num in nums:
            if num % 3 == 1:
                rem1.append(num)
            elif num % 3 == 2:
                rem2.append(num)

        rem1.sort()
        rem2.sort()

        if total % 3 == 0:
            return total

        elif total % 3 == 1:
            # Option 1: Remove smallest remainder-1 number
            option1 = rem1[0] if rem1 else float('inf')

            # Option 2: Remove two smallest remainder-2 numbers
            option2 = rem2[0] + rem2[1] if len(rem2) >= 2 else float('inf')

            return total - min(option1, option2)

        else:  # total % 3 == 2
            # Option 1: Remove smallest remainder-2 number
            option1 = rem2[0] if rem2 else float('inf')

            # Option 2: Remove two smallest remainder-1 numbers
            option2 = rem1[0] + rem1[1] if len(rem1) >= 2 else float('inf')

            return total - min(option1, option2)
