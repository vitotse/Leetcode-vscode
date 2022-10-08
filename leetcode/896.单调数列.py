#
# @lc app=leetcode.cn id=896 lang=python3
#
# [896] 单调数列
#

# @lc code=start

class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        
        N = len(nums)
        inc, dec = True, True
        for i in range(1, N):
            if nums[i] < nums[i - 1]:
                inc = False
            if nums[i] > nums[i - 1]:
                dec = False
            if not inc and not dec:
                return False
        return True


# @lc code=end

