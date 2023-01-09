#
# @lc app=leetcode.cn id=80 lang=python3
#
# [80] 删除有序数组中的重复项 II
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return n
        fast, slow = 2,2

        while fast < n:
            if not nums[slow - 2] == nums[fast]:
                nums[slow] = nums[fast]
                slow += 1

            fast += 1

        return slow




# @lc code=end

