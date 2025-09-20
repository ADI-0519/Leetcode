class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        a = []
        
        row,col = len(matrix),len(matrix[0])
        i,j = 0,0

        direction = "RIGHT"

        UP_WALL = 0
        RIGHT_WALL = col
        LEFT_WALL = -1
        DOWN_WALL = row

        while len(a) != (row*col):

            if direction == "RIGHT":
                while j < RIGHT_WALL:
                    a.append(matrix[i][j])
                    j += 1

                i,j = i+1,j-1
                RIGHT_WALL -= 1
                direction = "DOWN"

            elif direction == "DOWN":
                while i < DOWN_WALL:
                    a.append(matrix[i][j])
                    i += 1

                i, j = i-1,j-1
                DOWN_WALL -= 1
                direction = "LEFT"

            elif direction == "LEFT":
                while j > LEFT_WALL:
                    a.append(matrix[i][j])
                    j -= 1

                i,j = i-1,j+1
                LEFT_WALL += 1
                direction = "UP"

            else:
                while i > UP_WALL:
                    a.append(matrix[i][j])
                    i -= 1

                i,j = i+1,j+1
                UP_WALL += 1
                direction = "RIGHT"

        return a

           