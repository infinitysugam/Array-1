# We use 4 pointer and based on that we perform the traversal
# Time Complexity = O(m*n)
# Space Complexity = O(1)

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        row = 0
        col = 0 
        result = []

        top = 0
        left = 0
        bottom = m-1
        right = n-1

        while (top <= bottom and left<=right):
            for i in range(left,right+1):
                result.append(matrix[top][i])
            top = top + 1

            if (top <= bottom and left<=right):
                for i in range(top,bottom+1):
                    result.append(matrix[i][right])
                right = right -1

            if (top <= bottom and left<=right):

                for i in range(right,left-1,-1):
                    result.append(matrix[bottom][i])
                bottom = bottom-1
            if (top <= bottom and left<=right):

                for i in range(bottom,top-1,-1):
                    result.append(matrix[i][left])
                left = left +1
        return result




        