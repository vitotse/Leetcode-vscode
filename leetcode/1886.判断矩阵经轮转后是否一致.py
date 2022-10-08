#
# @lc app=leetcode.cn id=1886 lang=python3
#
# [1886] 判断矩阵经轮转后是否一致
#

# @lc code=start
class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n = len(mat)
        # 最多旋转 4 次
        for k in range(4):
            # 旋转操作
            for i in range(n // 2):
                for j in range((n + 1) // 2):
                    mat[i][j], mat[n-1-j][i], mat[n-1-i][n-1-j], mat[j][n-1-i] \
                        = mat[n-1-j][i], mat[n-1-i][n-1-j], mat[j][n-1-i], mat[i][j]
            
            if mat == target:
                return True
        return False
        
# @lc code=end

