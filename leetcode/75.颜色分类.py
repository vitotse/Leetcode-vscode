#
# @lc app=leetcode.cn id=75 lang=python3
#
# [75] 颜色分类
#

# @lc code=start
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # 替换的helper
        def swap(nums: List[int], index1, index2):
            nums[index1], nums[index2] = nums[index2], nums[index1]

        size = len(nums)
        if size < 2:
            return

        zero_index = -1
        two_index = size - 1

        i = 0
        while i <= two_index:
            # 0 的分组
            if nums[i] == 0:
                zero_index += 1
                swap(nums, i, zero_index)
                i += 1

            # 1 的分组
            elif nums[i] == 1:
                i += 1

            # 2 的分组
            else:
                swap(nums, i, two_index)
                two_index -= 1


# @lc code=end

