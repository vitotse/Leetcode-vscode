#
# @lc app=leetcode.cn id=260 lang=python3
#
# [260] 只出现一次的数字 III
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        if len(nums) < 2:
            return []
        diff = 0
        for num in nums:
            diff ^= num
        diff &= -1 * diff
        num1, num2 = 0,0
        for num in nums:
            if (num & diff) == 0:
                num1 ^= num
            else:
                num2 ^= num
        return [num1, num2]

# @lc code=end

