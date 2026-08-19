class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        rows, cols = len(box), len(box[0])
        
        for row in range(rows):
            emptySpot = cols - 1
            for col in reversed(range(cols)):
                if box[row][col] == "#":
                    box[row][col], box[row][emptySpot] = box[row][emptySpot], box[row][col]
                    emptySpot -= 1
                elif box[row][col] == "*":
                    emptySpot = col - 1
        
        rotatedBox = []

        for col in range(cols):
            newCol = []
            for row in reversed(range(rows)):
                newCol.append(box[row][col])
            rotatedBox.append(newCol)
        
        return rotatedBox
