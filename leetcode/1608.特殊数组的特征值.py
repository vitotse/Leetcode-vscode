#
# @lc app=leetcode.cn id=1608 lang=python3
#
# [1608] 特殊数组的特征值
#

# @lc code=start
class Solution:
    def specialArray(self, nums: List[int]) -> int:

        n = len(nums)
        nums.sort()

        left, right = 0, n

        while left <= right:

            mid = (left + right) // 2

            count = 0

            for i in range(n):
                if nums[i] >= mid:
                    count += 1

            if count > mid:
                left = mid + 1
            elif count < mid:
                right = mid - 1
            else:
                return mid

        return -1



# @lc code=end

