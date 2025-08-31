from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        # Fill sets with the given numbers
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    num = board[i][j]
                    rows[i].add(num)
                    cols[j].add(num)
                    boxes[(i // 3) * 3 + j // 3].add(num)

        def backtrack(r=0, c=0) -> bool:
            # Find next empty cell
            while r < 9 and board[r][c] != ".":
                c += 1
                if c == 9:
                    r += 1
                    c = 0
            if r == 9:  # Solved
                return True

            box_idx = (r // 3) * 3 + c // 3
            for ch in map(str, range(1, 10)):
                if ch not in rows[r] and ch not in cols[c] and ch not in boxes[box_idx]:
                    # Place number
                    board[r][c] = ch
                    rows[r].add(ch)
                    cols[c].add(ch)
                    boxes[box_idx].add(ch)

                    if backtrack(r, c):
                        return True

                    # Undo (backtrack)
                    board[r][c] = "."
                    rows[r].remove(ch)
                    cols[c].remove(ch)
                    boxes[box_idx].remove(ch)

            return False

        backtrack()
