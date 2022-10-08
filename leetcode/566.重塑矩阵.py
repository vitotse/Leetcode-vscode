#
# @lc app=leetcode.cn id=566 lang=python3
#
# [566] 重塑矩阵
#

# @lc code=start
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        
        m, n = len(mat), len(mat[0])
        if m*n != r*c:
            return mat
        ans = [[0]*c for _ in range(r)]
        for i in range(m):
            for j in range(n):
                k = i*n+j
                ans[k//c][k%c] = mat[i][j]
        return ans

# @lc code=end

