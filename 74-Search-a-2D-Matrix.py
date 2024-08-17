class Solution(object):
    def searchMatrix(self, matrix, target):
        \\\
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        \\\
        L = 0
        R = len(matrix) - 1

        while L <= R:


            mid = int(float((L+R)/2))
           
            if matrix[mid][-1] < target:
                L += 1
            elif matrix[mid][-1] > target:
                R -= 1
            else:
                return True
            
        L1 = 0
        R1 = len(matrix[0]) -1

        while L1 <= R1:

            midrow = int(float((L1+R1)/2))

            if matrix[mid][midrow] < target:
                L1 += 1
            elif matrix[mid][midrow] > target:
                R1 -= 1
            else:
                return True
        
        return False

