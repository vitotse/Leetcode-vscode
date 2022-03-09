#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子数组和
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        pre = 0
        max_ans = nums[0]

        for i in range(len(nums)):
            pre = max(nums[i], pre + nums[i])
            max_ans = max(pre, max_ans)

        return max_ans
# @lc code=end

