#
# @lc app=leetcode.cn id=59 lang=python3
#
# [59] 螺旋矩阵 II
#

# @lc code=start
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:

        left,right,top,bottom = 0,n-1,0,n-1

        matrix = [[0 for _ in range(n)] for _ in range(n)]
        num, target = 1, n*n
        while num <= target:
            # left to right
            for i in range(left, right+1):
                matrix[top][i] = num
                num += 1

            top += 1

            # top to bottom
            for i in range(top,bottom+1):
                matrix[i][right] = num
                num += 1

            right -= 1

            # right to left
            for i in range(right,left-1, -1):
                matrix[bottom][i] = num
                num += 1

            bottom -= 1

            # bottom to top
            for i in range(bottom,top - 1, -1):
                matrix[i][left] = num
                num += 1

            left += 1

        return matrix
# @lc code=end

