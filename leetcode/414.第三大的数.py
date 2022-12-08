#
# @lc app=leetcode.cn id=414 lang=python3
#
# [414] 第三大的数
#

# @lc code=start
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        diff = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                diff += 1
                if diff == 3:  # 此时 nums[i] 就是第三大的数
                    return nums[i]
        return nums[0]

# @lc code=end

