class Solution:
    def kthCharacter(self, k: int, operations: list[int]) -> str:
        # Step 1: Track the length of the word after each operation
        lengths = [1]  # word starts as "a"
        for op in operations:
            lengths.append(lengths[-1] * 2)

        # Step 2: Work backwards to trace k back to original "a"
        shifts = 0  # how many times the character is shifted (mod 26)
        for i in reversed(range(len(operations))):
            half = lengths[i]
            op = operations[i]

            if k > half:
                k -= half  # move to second half
                if op == 1:
                    shifts += 1  # will need to shift character by 1
                # if op == 0: do nothing, it's identical to the first half
            # else, k stays as is (first half), no action needed

        # Step 3: Only 'a' is at the start; apply shifts
        final_char = chr((ord('a') - ord('a') + shifts) % 26 + ord('a'))
        return final_char
