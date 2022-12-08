#
# @lc app=leetcode.cn id=131 lang=python3
#
# [131] 分割回文串
#

# @lc code=start
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        self.isPalindrome = lambda s : s == s[::-1]
        res = []
        self.backtrack(s, res, [])
        return res
        
    def backtrack(self, s, res, path):
        if not s:
            res.append(path)
            return
        for i in range(1, len(s) + 1): #注意起始和结束位置
            if self.isPalindrome(s[:i]):
                self.backtrack(s[i:], res, path + [s[:i]])


# @lc code=end

