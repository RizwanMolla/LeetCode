class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        power_set = {"".join(sorted(str(1 << i))) for i in range(31)}
        return "".join(sorted(str(n))) in power_set
