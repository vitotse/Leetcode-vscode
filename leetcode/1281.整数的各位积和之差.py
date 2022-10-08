#
# @lc app=leetcode.cn id=1281 lang=python3
#
# [1281] 整数的各位积和之差
#

# @lc code=start
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sum = 0
        mul = 1

        num = 0
        while n > 0:
            num = n % 10
            n = n // 10
            mul *= num
            sum += num

        return mul - sum



# @lc code=end

