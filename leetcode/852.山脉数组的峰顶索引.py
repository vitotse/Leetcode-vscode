#
# @lc app=leetcode.cn id=852 lang=python3
#
# [852] 山脉数组的峰顶索引
#

# @lc code=start

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        n = len(arr)
        left, right, ans = 1, n - 2, 0

        while left <= right:
            mid = (left + right) // 2

            if arr[mid] > arr[mid + 1]:
                ans = mid
                right = mid - 1

            else:
                left = mid + 1

        return ans


# @lc code=end

