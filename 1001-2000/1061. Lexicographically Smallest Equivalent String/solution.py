class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        parent = [i for i in range(26)]  # Union-Find for 'a' to 'z'

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])  # Path compression
            return parent[x]

        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX == rootY:
                return
            # Always keep the smaller character as the root
            if rootX < rootY:
                parent[rootY] = rootX
            else:
                parent[rootX] = rootY

        # Step 1: Union all pairs
        for a, b in zip(s1, s2):
            union(ord(a) - ord('a'), ord(b) - ord('a'))

        # Step 2: Transform baseStr using the smallest equivalent character
        result = []
        for ch in baseStr:
            smallest_equiv_char = chr(find(ord(ch) - ord('a')) + ord('a'))
            result.append(smallest_equiv_char)

        return ''.join(result)
