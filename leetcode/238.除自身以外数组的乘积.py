#
# @lc app=leetcode.cn id=238 lang=python3
#
# [238] 除自身以外数组的乘积
#

# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res, p, q = [1], 1, 1
        for i in range(len(nums) - 1):
            p *= nums[i]
            res.append(p)

        for i in range(len(nums) -1, 0, -1):
            q *= nums[i]
            res[i - 1] *= q

        return res
# @lc code=end

