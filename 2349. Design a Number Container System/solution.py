import bisect

class NumberContainers:

    def __init__(self):
        self.index_to_num = {}
        self.num_to_indices = {}

    def change(self, index: int, number: int) -> None:
        if index in self.index_to_num:
            old_num = self.index_to_num[index]
            if old_num in self.num_to_indices:
                indices = self.num_to_indices[old_num]
                if index in indices:
                    indices.remove(index)
                    if not indices:
                        del self.num_to_indices[old_num]
        self.index_to_num[index] = number
        if number not in self.num_to_indices:
            self.num_to_indices[number] = []
        bisect.insort(self.num_to_indices[number], index)

    def find(self, number: int) -> int:
        if number in self.num_to_indices and self.num_to_indices[number]:
            return self.num_to_indices[number][0]
        return -1
        


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)