#
# @lc app=leetcode.cn id=119 lang=python3
#
# [119] 杨辉三角 II
#

# @lc code=start
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [1] * (rowIndex + 1)
        for i in range(2, rowIndex + 1):
            # 从后往前推算，不影响答案
            for j in range(i - 1, 0, -1):
                res[j] += res[j - 1]
        return res


# @lc code=end

