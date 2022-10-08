#
# @lc app=leetcode.cn id=1630 lang=python3
#
# [1630] 等差子数组
#

# @lc code=start
class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        def check():
            n = len(lst)
            diff = lst[1] - lst[0]
            for j in range(2, n):
                if lst[j] - lst[j - 1] != diff:
                    return False
            return True

        ans = []
        for i, left in enumerate(l):
            lst = nums[left: r[i] + 1]
            lst.sort()
            ans.append(check())
        return ans


# @lc code=end

