#
# @lc app=leetcode.cn id=45 lang=python3
#
# [45] 跳跃游戏 II
#

# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:

        num, max_num = 0, 0
        steps = 0
        for i in range(len(nums) - 1):
            max_num = max(max_num, nums[i] + i)
            if i == num:
                num = max_num
                steps += 1
        return steps

# @lc code=num

