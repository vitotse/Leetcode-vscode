#
# @lc app=leetcode.cn id=1005 lang=python3
#
# [1005] K 次取反后最大化的数组和
#

# @lc code=start
class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort()

        neg = 0

        for num in nums:
            if num < 0:
                neg += 1

        for i in range(min(neg,k)):
            nums[i] = -nums[i]

        rest = k-min(neg, k)
        if rest % 2 == 0:
            return sum(nums)
        return sum(nums) - 2*min(nums)
# @lc code=end

