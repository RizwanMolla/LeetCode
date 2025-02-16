class Solution:
    def constructDistancedSequence(self, n: int) -> list[int]:
        size = 2 * n - 1
        result = [0] * size
        used = [False] * (n + 1)

        def backtrack(index):
            if index == size:
                return True
            
            if result[index] != 0:
                return backtrack(index + 1)
            
            for num in range(n, 0, -1):
                if used[num]:
                    continue
                
                if num == 1:
                    result[index] = 1
                    used[1] = True
                    if backtrack(index + 1):
                        return True
                    result[index] = 0
                    used[1] = False
                else:
                    if index + num < size and result[index + num] == 0:
                        result[index] = result[index + num] = num
                        used[num] = True
                        if backtrack(index + 1):
                            return True
                        result[index] = result[index + num] = 0
                        used[num] = False

            return False

        backtrack(0)
        return result