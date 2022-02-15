#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除有序数组中的重复项
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        left = 0
        for right in range(len(nums)):
            if nums[left] != nums[right]:
                left += 1
                nums[left] = nums[right]

        return left + 1

# @lc code=end

