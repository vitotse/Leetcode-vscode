#
# @lc app=leetcode.cn id=334 lang=python3
#
# [334] 递增的三元子序列
#

# @lc code=start
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:

        n = len(nums)
        if n < 3:
            return False

        first, second = nums[0], float('inf')
        for i in range(1, n):
            num = nums[i]
            if num > second:
                return True
            if num > first:
                second = num
            else:
                first = num
            
        return False

# @lc code=end

