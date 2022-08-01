#
# @lc app=leetcode.cn id=633 lang=python3
#
# [633] 平方数之和
#

# @lc code=start
class Solution:
    def judgeSquareSum(self, c: int) -> bool:

        num = int(sqrt(c))
        for i in range(num + 1):
            left, right = 0, num
            while left <= right:
                mid = (left + right) // 2
                if i * i + mid * mid == c:
                    return True
                elif i * i + mid * mid > c:
                    right = mid - 1
                else:
                    left = mid + 1
        return False

# @lc code=end

