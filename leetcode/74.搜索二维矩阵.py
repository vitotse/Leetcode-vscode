#
# @lc app=leetcode.cn id=74 lang=python3
#
# [74] 搜索二维矩阵
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        m, n = len(matrix), len(matrix[0])

        low, high = 0, m * n -1

        while low <= high:
            mid = (high - low) // 2 + low

            x = matrix[mid // n][mid % n]
            if x < target:
                low = mid + 1
            elif x > target:
                high = mid - 1
            else:
                return True

        return False


# @lc code=end

