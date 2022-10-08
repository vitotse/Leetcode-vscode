#
# @lc app=leetcode.cn id=989 lang=python3
#
# [989] 数组形式的整数加法
#

# @lc code=start

import math

class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:

        return [int(i) for i in list(str(int(''.join([str(i) for i in num])) + k))]


# @lc code=end

