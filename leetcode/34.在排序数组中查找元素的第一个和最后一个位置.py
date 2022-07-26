#
# @lc app=leetcode.cn id=34 lang=python3
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#

# @lc code=start

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = bisect.bisect_left(nums,target)
        if left == len(nums) or nums[left] != target:
            return [-1,-1]
        right = bisect.bisect_right(nums,target)
        return [left,right - 1]


# @lc code=end

