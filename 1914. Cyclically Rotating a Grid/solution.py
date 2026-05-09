class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        top = 0
        left = 0
        bot = len(grid) - 1
        right = len(grid[0]) - 1
        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        while top < bot and left < right:
            n = ((bot - top) * 2) + ((right - left) * 2)
            rot = k % n

            for i in range(rot):
                hold = grid[top][left]
                y = top
                x = left
                d = 0

                for j in range(n - 1):
                    [dy, dx] = dirs[d]
                    [ny, nx] = [y + dy, x + dx]

                    if ny < top or ny > bot or nx < left or nx > right:
                        d = (d + 1) % 4
                        [dy, dx] = dirs[d]
                        [ny, nx] = [y + dy, x + dx]

                    grid[y][x] = grid[ny][nx]
                    [y, x] = [ny, nx]

                grid[top + 1][left] = hold

            top += 1
            left += 1
            bot -= 1
            right -= 1

        return grid