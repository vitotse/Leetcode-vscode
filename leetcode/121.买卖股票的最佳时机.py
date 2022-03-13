#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#

# @lc code=start
import sys

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min = sys.maxsize
        max = 0
        for price in prices:
            if price < min:
                min = price
            elif price - min > max:
                max = price - min

        return max

# @lc code=end

