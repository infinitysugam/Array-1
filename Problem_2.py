# For this we calculate the next index based on the conditions and put that element into resultant array
#Time Complexity = O(m*n)
# Space Complexity = O(1)
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m = len(mat)
        n = len(mat[0])
        dir = True  # True means going up-right
        row = 0
        col = 0 
        result = []

        while len(result) != m * n:
            result.append(mat[row][col])
            
            if dir:
                if col == n - 1:
                    row += 1
                    dir = False
                elif row == 0:
                    col += 1
                    dir = False
                else:
                    row -= 1
                    col += 1
            else:
                if row == m - 1:
                    col += 1
                    dir = True
                elif col == 0:
                    row += 1
                    dir = True
                else:
                    row += 1
                    col -= 1

        return result
