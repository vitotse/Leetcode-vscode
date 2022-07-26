#
# @lc app=leetcode.cn id=441 lang=python3
#
# [441] 排列硬币
#

# @lc code=start
class Solution:
    def arrangeCoins(self, n: int) -> int:
        left, right = 0,n

        while left < right:
            mid = (left + right + 1) // 2
            
            # 前一排，等差求和
            if mid * (mid + 1) <= 2 * n:
                left = mid
            else:
                right = mid - 1

        return left


# @lc code=end

