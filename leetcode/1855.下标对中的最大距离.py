#
# @lc app=leetcode.cn id=1855 lang=python3
#
# [1855] 下标对中的最大距离
#

# @lc code=start

class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:

        res = 0
        for index, value in enumerate(nums1):
            i, j = -1, len(nums2)
            while i + 1 != j:
                mid = (i + j) >> 1
                if nums2[mid] >= value:
                    i = mid
                else:
                    j = mid
            res = max(res, i - index)
        return res


# @lc code=end

