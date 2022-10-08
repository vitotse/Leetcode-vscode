#
# @lc app=leetcode.cn id=976 lang=python3
#
# [976] 三角形的最大周长
#

# @lc code=start
class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        return next((x+y+z for x, y, z in zip(nums, nums[1:], nums[2:]) if x<y+z), 0)


# @lc code=end

