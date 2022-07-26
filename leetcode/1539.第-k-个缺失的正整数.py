#
# @lc app=leetcode.cn id=1539 lang=python3
#
# [1539] 第 k 个缺失的正整数
#

# @lc code=start

from re import L


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:

        left, right = 0, len(arr)

        while left < right:
            mid = (left + right) // 2

            if arr[mid] - mid - 1 < k:
                left = mid + 1
            else:
                right = mid

        return k + left


# @lc code=end

