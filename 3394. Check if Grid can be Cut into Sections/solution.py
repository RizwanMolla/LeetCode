class Solution:
    def checkValidCuts(self, n: int, rectangles: list[list[int]]) -> bool:
        def check_vertical():
            sorted_rects = sorted(rectangles, key=lambda x: x[0])
            m = len(sorted_rects)
            if m < 3:
                return False
            prefix_max_end = []
            current_max = 0
            for rect in sorted_rects:
                current_max = max(current_max, rect[2])
                prefix_max_end.append(current_max)
            
            split_i = -1
            for i in range(m - 1):
                if sorted_rects[i + 1][0] >= prefix_max_end[i]:
                    split_i = i
                    break
            if split_i == -1:
                return False
            remaining = sorted_rects[split_i + 1:]
            if len(remaining) < 2:
                return False
            
            current_max = 0
            for j in range(len(remaining) - 1):
                current_max = max(current_max, remaining[j][2])
                if remaining[j + 1][0] >= current_max:
                    return True
            return False
        
        def check_horizontal():
            sorted_rects = sorted(rectangles, key=lambda x: x[1])
            m = len(sorted_rects)
            if m < 3:
                return False
            prefix_max_endy = []
            current_maxy = 0
            for rect in sorted_rects:
                current_maxy = max(current_maxy, rect[3])
                prefix_max_endy.append(current_maxy)
            
            split_i = -1
            for i in range(m - 1):
                if sorted_rects[i + 1][1] >= prefix_max_endy[i]:
                    split_i = i
                    break
            if split_i == -1:
                return False
            remaining = sorted_rects[split_i + 1:]
            if len(remaining) < 2:
                return False
            
            current_maxy = 0
            for j in range(len(remaining) - 1):
                current_maxy = max(current_maxy, remaining[j][3])
                if remaining[j + 1][1] >= current_maxy:
                    return True
            return False
        
        return check_vertical() or check_horizontal()