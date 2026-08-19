class Solution:
    def maxDiff(self, num: int) -> int:
        num_str = str(num)

        # Maximize a: Replace first non-9 digit with 9
        for digit in num_str:
            if digit != '9':
                a = int(num_str.replace(digit, '9'))
                break
        else:
            a = num  # all digits are 9 already

        # Minimize b:
        first_digit = num_str[0]
        if first_digit != '1':
            b = int(num_str.replace(first_digit, '1'))
        else:
            for i in range(1, len(num_str)):
                if num_str[i] != '0' and num_str[i] != '1':
                    b = int(num_str.replace(num_str[i], '0'))
                    break
            else:
                b = num  # nothing to replace

        return a - b
