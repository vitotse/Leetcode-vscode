#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#

# @lc code=start

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return n

        dp1 = 1
        dp2 = 2
        for i in range(3, n+1):
            sum = dp1 + dp2
            dp1, dp2 = dp2, sum

        return dp2
# @lc code=end

