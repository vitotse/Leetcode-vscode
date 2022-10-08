#
# @lc app=leetcode.cn id=389 lang=python3
#
# [389] 找不同
#

# @lc code=start
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        cnt1 = Counter(s)
        cnt2 = Counter(t)
        for va in cnt2:
            if cnt2[va] > cnt1[va]:
                return va

# @lc code=end

