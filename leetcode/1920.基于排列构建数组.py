#
# @lc app=leetcode.cn id=1920 lang=python3
#
# [1920] 基于排列构建数组
#

# @lc code=start
class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        return [nums[nums[_]] for _ in range(n)]
# @lc code=end

