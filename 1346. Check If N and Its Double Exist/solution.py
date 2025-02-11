class Solution:
    def checkIfExist(self, arr):
        seen_numbers = set()
        for ele in arr:
            if 2 * ele in seen_numbers or (ele % 2 == 0 and ele // 2 in seen_numbers):
                return True
            seen_numbers.add(ele)
        return False