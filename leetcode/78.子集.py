#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] 子集
#

# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        size = len(nums)
        marks = [1<<i for i in range(size)]
        ans = []

        for case in range(2**size):
            arr = []
            for i, mark in enumerate(marks):
                if case&mark:
                    arr.append(nums[i])

            ans.append(arr)

        return ans

# @lc code=end

