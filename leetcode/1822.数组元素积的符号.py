#
# @lc app=leetcode.cn id=1822 lang=python3
#
# [1822] 数组元素积的符号
#

# @lc code=start
class Solution:
    def arraySign(self, nums: List[int]) -> int:

        neg_count = 0

        for n in nums:
            if n < 0: neg_count += 1
            elif n == 0: return 0


        if neg_count % 2 == 1: return -1

        return 1
            


# @lc code=end

