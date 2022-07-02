#
# @lc app=leetcode.cn id=746 lang=python3
#
# [746] 使用最小花费爬楼梯
#

# @lc code=start
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp0 = cost[0]
        dp1 = cost[1]

        for i in range(2, len(cost)):
            dpi = min(dp0, dp1) + cost[i]
            dp0 = dp1
            dp1 = dpi

        return min(dp0, dp1)
# @lc code=end

