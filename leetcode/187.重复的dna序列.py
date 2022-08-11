#
# @lc app=leetcode.cn id=187 lang=python3
#
# [187] 重复的DNA序列
#

# @lc code=start
from collections import defaultdict


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        dict = defaultdict(int)
        l = 10
        ans = []

        for i in range(len(s) - l+1):
            dict[s[i:i+l]] += 1

            if dict[s[i:i+l]] == 2:
                ans.append(s[i:i+l])

        return ans
# @lc code=end

