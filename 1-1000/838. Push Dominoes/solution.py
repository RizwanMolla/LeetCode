class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        n = len(dominoes)
        forces = [0] * n

        # Left to right pass for 'R' forces
        force = 0
        for i in range(n):
            if dominoes[i] == 'R':
                force = n  # Start with a large force
            elif dominoes[i] == 'L':
                force = 0  # No force from right when there's an L
            else:
                force = max(force - 1, 0)
            forces[i] += force

        # Right to left pass for 'L' forces
        force = 0
        for i in range(n - 1, -1, -1):
            if dominoes[i] == 'L':
                force = n
            elif dominoes[i] == 'R':
                force = 0
            else:
                force = max(force - 1, 0)
            forces[i] -= force

        # Build final result
        result = []
        for f in forces:
            if f > 0:
                result.append('R')
            elif f < 0:
                result.append('L')
            else:
                result.append('.')

        return ''.join(result)
