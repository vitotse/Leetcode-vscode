#
# @lc app=leetcode.cn id=1790 lang=python3
#
# [1790] 仅执行一次字符串交换能否使两个字符串相等
#

# @lc code=start
class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        return s1 == s2 or Counter(s1) == Counter(s2) and sum(s1[i] != s2[i]  for i in range(len(s1))) == 2
# @lc code=end

