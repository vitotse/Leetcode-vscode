#
# @lc app=leetcode.cn id=54 lang=python3
#
# [54] 螺旋矩阵
#

# @lc code=start
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        # 初始化
        x, y = 0, 0
        dx, dy = dirs.pop(0)
        dirs.append((dx, dy))
        res = []

        # 逆时针循环
        while len(res) < m*n:
            res.append(matrix[x][y])
            matrix[x][y] = -101
            if not(0<=x+dx<=m-1 and 0<= y+dy <= n-1 and matrix[x+dx][y+dy] != -101):
                dx, dy = dirs.pop(0)
                dirs.append((dx, dy))
            x, y = x + dx, y + dy
        return res


# @lc code=end

