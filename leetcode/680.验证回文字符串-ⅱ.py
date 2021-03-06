#
# @lc app=leetcode.cn id=680 lang=python3
#
# [680] 验证回文字符串 Ⅱ
#

# @lc code=start

class Solution:
    def validPalindrome(self, s: str) -> bool:
        def chekcPalindrome(low, high):
            i, j = low, high
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        low, high = 0, len(s) - 1
        while low < high:
            if s[low] == s[high]:
                low += 1
                high -= 1
            else:
                # 可以删除一个字符
                return chekcPalindrome(low + 1, high) or chekcPalindrome(low, high - 1)
        return True

# @lc code=end

