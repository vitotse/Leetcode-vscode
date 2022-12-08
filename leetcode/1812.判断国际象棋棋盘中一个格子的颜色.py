#
# @lc app=leetcode.cn id=1812 lang=python3
#
# [1812] 判断国际象棋棋盘中一个格子的颜色
#

# @lc code=start
class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:

        col = coordinates[0]
        row = coordinates[1]

        colN = ord(col) % 2
        rowN = int(row) % 2

        if not colN == rowN:
            return True

        return False


# @lc code=end

