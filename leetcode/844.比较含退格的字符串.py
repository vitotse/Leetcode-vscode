#
# @lc app=leetcode.cn id=844 lang=python3
#
# [844] 比较含退格的字符串
#

# @lc code=start
from email import charset
import string
from tokenize import String


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        a = ""
        b = ""
        for sc in s:

            if sc == '#':
                a = a[:-1]
            else:
                a += sc

        for tc in t:
            if tc == '#':
                b = b[:-1]
            else:
                b += tc

        if a == b:
            return True

        return False


# @lc code=end

