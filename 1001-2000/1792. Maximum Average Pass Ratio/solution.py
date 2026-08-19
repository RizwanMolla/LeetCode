import heapq

class Solution:
    def maxAverageRatio(self, classes: list[list[int]], extra_students: int) -> float:
        max_heap = []

        def calculate_gain(pass_count, total_count):
            current_ratio = pass_count / total_count
            new_ratio = (pass_count + 1) / (total_count + 1)
            return new_ratio - current_ratio

        for idx, (pass_count, total_count) in enumerate(classes):
            gain = calculate_gain(pass_count, total_count)
            heapq.heappush(max_heap, (-gain, idx))

        while extra_students > 0:
            _, class_index = heapq.heappop(max_heap)
            classes[class_index][0] += 1
            classes[class_index][1] += 1
            gain = calculate_gain(classes[class_index][0], classes[class_index][1])
            heapq.heappush(max_heap, (-gain, class_index))
            extra_students -= 1

        total_avg_ratio = sum(pass_count / total_count for pass_count, total_count in classes)
        return total_avg_ratio / len(classes)
