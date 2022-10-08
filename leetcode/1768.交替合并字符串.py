#
# @lc app=leetcode.cn id=1768 lang=python3
#
# [1768] 交替合并字符串
#

# @lc code=start
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        m, n = len(word1), len(word2)
        ans = ""
        i = 0
        j = 0
        order = 1
        while i<m and j<n:
            if order:
                ans += word1[i]
                i += 1
            else:
                ans += word2[j]
                j += 1
            order = 1- order
        ans += word1[i:] + word2[j:]
        return ans

# @lc code=end

