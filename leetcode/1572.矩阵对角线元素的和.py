#
# @lc app=leetcode.cn id=1572 lang=python3
#
# [1572] 矩阵对角线元素的和
#

# @lc code=start
class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:

        sum = 0

        leng = len(mat)
        print(leng)

        for i in range(0,leng):
            print(i)
        
            sum += mat[i][i]
            sum += mat[i][leng-i-1]


        if leng % 2 == 1:
            half = leng // 2
            sum -= mat[half][half]


        return sum

# @lc code=end

