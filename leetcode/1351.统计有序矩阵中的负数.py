#
# @lc app=leetcode.cn id=1351 lang=python3
#
# [1351] 统计有序矩阵中的负数
#

# @lc code=start
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        non_negtive = 0
        m = len(grid)
        n = len(grid[0])
        l = 0
        r = n - 1
        for row in range(m):
            l = 0
            while l < r:
                mid = (l + r + 1) // 2
                if grid[row][mid] >= 0:
                    l = mid
                else:
                    r = mid - 1
            if r == 0 and grid[row][r] < 0:  
                break  
            non_negtive += (r + 1)

        return m * n - non_negtive

# @lc code=end

