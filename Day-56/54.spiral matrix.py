class Solution(object):
    def spiralOrder(self, matrix):

        top = 0
        bottom = len(matrix) - 1

        left = 0
        right = len(matrix[0]) - 1
        
        lt = []

        while top <= bottom and left <= right:

            for i in range(left, right + 1):
                lt.append(matrix[top][i])
            top += 1
            
            for j in range(top, bottom + 1):
                lt.append(matrix[j][right])
            right -= 1

            if top <= bottom:

                for k in range(right, left - 1, -1):
                    lt.append(matrix[bottom][k])
                bottom -= 1

            if left <= right:

                for l in range(bottom, top - 1 , -1):
                    lt.append(matrix[l][left])
                left += 1
        return lt