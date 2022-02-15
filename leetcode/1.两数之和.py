#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
from operator import index


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for index1 in range(n):
            for index2 in range(index1 + 1,n):
                if nums[index1] + nums [index2] == target:
                    return [index1, index2]

        return []
# @lc code=end

