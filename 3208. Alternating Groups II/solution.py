class Solution:
    def numberOfAlternatingGroups(self, colors: list[int], k: int) -> int:
        size = len(colors)
        ans = count = 0
        
        for i in range(size << 1):
            if i and colors[i % size] == colors[(i - 1) % size]:
                count = 1
            else:
                count += 1
            ans += i >= size and count >= k
        return ans