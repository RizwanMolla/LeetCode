class Node:
    __slots__ = ("left", "right", "cover_count", "covered_length")

    def __init__(self):
        self.left = self.right = 0
        self.cover_count = 0
        self.covered_length = 0


class SegmentTree:
    def __init__(self, coords):
        size = len(coords) - 1
        self.coords = coords
        self.tree = [Node() for _ in range(size << 2)]
        self.build(1, 0, size - 1)

    def build(self, index, left, right):
        self.tree[index].left = left
        self.tree[index].right = right
        if left != right:
            mid = (left + right) >> 1
            self.build(index << 1, left, mid)
            self.build(index << 1 | 1, mid + 1, right)

    def update(self, index, update_left, update_right, value):
        node = self.tree[index]
        if node.left >= update_left and node.right <= update_right:
            node.cover_count += value
        else:
            mid = (node.left + node.right) >> 1
            if update_left <= mid:
                self.update(index << 1, update_left, update_right, value)
            if update_right > mid:
                self.update(index << 1 | 1, update_left, update_right, value)
        self.pull_up(index)

    def pull_up(self, index):
        node = self.tree[index]
        if node.cover_count > 0:
            node.covered_length = (
                self.coords[node.right + 1] - self.coords[node.left]
            )
        elif node.left == node.right:
            node.covered_length = 0
        else:
            node.covered_length = (
                self.tree[index << 1].covered_length
                + self.tree[index << 1 | 1].covered_length
            )

    @property
    def total_length(self):
        return self.tree[1].covered_length


class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        x_coordinates = set()
        events = []

        for start_x, start_y, side_len in squares:
            end_x = start_x + side_len
            end_y = start_y + side_len
            x_coordinates.update([start_x, end_x])
            events.append((start_y, start_x, end_x, 1))
            events.append((end_y, start_x, end_x, -1))

        events.sort()
        sorted_coords = sorted(x_coordinates)
        seg_tree = SegmentTree(sorted_coords)
        coord_index = {x: i for i, x in enumerate(sorted_coords)}

        total_area = 0
        prev_y = 0

        for curr_y, x_start, x_end, delta in events:
            total_area += (curr_y - prev_y) * seg_tree.total_length
            seg_tree.update(1, coord_index[x_start], coord_index[x_end] - 1, delta)
            prev_y = curr_y

        half_area = total_area / 2
        accumulated_area = 0
        prev_y = 0

        for curr_y, x_start, x_end, delta in events:
            slice_area = (curr_y - prev_y) * seg_tree.total_length
            if accumulated_area + slice_area >= half_area:
                return prev_y + (half_area - accumulated_area) / seg_tree.total_length
            accumulated_area += slice_area
            seg_tree.update(1, coord_index[x_start], coord_index[x_end] - 1, delta)
            prev_y = curr_y

        return 0.0
