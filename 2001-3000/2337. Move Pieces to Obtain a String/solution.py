class Solution:
    def move_next(self, sequence, length, index):
        while index < length and sequence[index] == '_':
            index += 1
        return index

    def canChange(self, initial: str, target: str) -> bool:
        size = len(initial)
        ptr1 = ptr2 = 0
        last_position = -1

        while ptr1 < size and ptr2 < size:
            ptr1 = self.move_next(initial, size, ptr1)
            ptr2 = self.move_next(target, size, ptr2)

            if ptr1 == size and ptr2 == size:
                return True
            if ptr1 == size or ptr2 == size or initial[ptr1] != target[ptr2]:
                return False

            if initial[ptr1] == 'L' and (ptr2 < last_position or ptr2 > ptr1):
                return False
            if initial[ptr1] == 'R' and ptr1 > ptr2:
                return False

            last_position = ptr2
            ptr1 += 1
            ptr2 += 1

        ptr1 = self.move_next(initial, size, ptr1)
        ptr2 = self.move_next(target, size, ptr2)

        return ptr1 == size and ptr2 == size
