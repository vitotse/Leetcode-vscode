#
# @lc app=leetcode.cn id=910 lang=python3
#
# [910] 最小差值 II
#

# @lc code=start
class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        nums.sort()
        mi, ma = nums[0], nums[-1]
        ans = ma - mi
        for i in range(len(nums) - 1):
            a, b = nums[i], nums[i+1]
            ans = min(ans, max(ma-k, a+k) - min(mi+k, b-k))
        return ans

# @lc code=end

