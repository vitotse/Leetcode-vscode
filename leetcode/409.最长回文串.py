#
# @lc app=leetcode.cn id=409 lang=python3
#
# [409] 最长回文串
#

# @lc code=start
import collections

class Solution:
    def longestPalindrome(self, s: str) -> int:
        ans = 0
        count = collections.Counter(s)
        for value in count.values():
            ans += value // 2 * 2
            if ans % 2 == 0 and value % 2 == 1:
                ans += 1
        return ans
# @lc code=end

