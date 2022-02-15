#
# @lc app=leetcode.cn id=16 lang=python3
#
# [16] 最接近的三数之和
#

# @lc code=start
import math


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        if n < 3: return 0

        ans = nums[0] + nums[1] + nums[2]
        for first in range(n-2):
            second = first + 1
            third = n - 1

            while second < third:
                sum = nums[first] + nums[second] + nums[third]

                if abs(sum - target) < abs(ans - target):
                    ans = sum

                if sum > target:
                    third -= 1
                else:
                    second += 1
                

        return ans


# @lc code=end

