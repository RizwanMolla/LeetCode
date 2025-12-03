from collections import defaultdict
from typing import List, Dict


class Solution:
	def countTrapezoids(self, points: List[List[int]]) -> int:
		"""Count number of trapezoids (improved variable names).

		points: list of [x, y]
		"""
		n = len(points)

		# slope_to_intercept_counts: slope -> (intercept -> count)
		slope_to_intercept_counts: Dict[float, Dict[float, int]] = defaultdict(lambda: defaultdict(int))
		# pair_key_to_slope_counts: pair_key -> (slope -> count)
		pair_key_to_slope_counts: Dict[int, Dict[float, int]] = defaultdict(lambda: defaultdict(int))

		INF_SLOPE = 1e9

		for idx1 in range(n):
			x1, y1 = points[idx1]
			for idx2 in range(idx1):
				x2, y2 = points[idx2]
				delta_x = x2 - x1
				delta_y = y2 - y1

				if delta_x == 0:
					slope = INF_SLOPE
					intercept = x1  # use x coordinate as identifier for vertical lines
				else:
					slope = delta_y / delta_x
					intercept = (y1 * delta_x - x1 * delta_y) / delta_x

				slope_to_intercept_counts[slope][intercept] += 1

				# pair_key encodes midpoint-like information for the pair
				pair_key = (x1 + x2 + 2000) * 4000 + (y1 + y2 + 2000)
				pair_key_to_slope_counts[pair_key][slope] += 1

		result = 0

		# For each slope, pick two distinct intercept groups: sum over combinations
		for group_counts in slope_to_intercept_counts.values():
			prefix_sum = 0
			for count in group_counts.values():
				result += prefix_sum * count
				prefix_sum += count

		# Subtract configurations where pairs share the same midpoint (collinear pairs)
		for group_counts in pair_key_to_slope_counts.values():
			prefix_sum = 0
			for count in group_counts.values():
				result -= prefix_sum * count
				prefix_sum += count

		return result

