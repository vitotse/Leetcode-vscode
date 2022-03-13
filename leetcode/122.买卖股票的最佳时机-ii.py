#
# @lc app=leetcode.cn id=122 lang=python3
#
# [122] 买卖股票的最佳时机 II
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        size = len(prices)

        dp = [0]*size
        for i in range(1,size):
            if prices[i]<=prices[i-1]: # 跌
                dp[i] = dp[i-1]
            if prices[i]>prices[i-1]: # 涨
                dp[i] = dp[i-1] + prices[i]-prices[i-1] # 之前的dp+差价

        return dp[-1]

# @lc code=end

