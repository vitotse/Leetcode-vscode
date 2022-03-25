#
# @lc app=leetcode.cn id=415 lang=python3
#
# [415] 字符串相加
#

# @lc code=start
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        carry = 0

        i, j = len(num1) - 1, len(num2) - 1

        ans = ""
        while i >= 0 or j >= 0:
            n1 = int(num1[i]) if i >= 0 else 0
            n2 = int(num2[j]) if j >= 0 else 0

            temp = n1 + n2 + carry

            carry = temp // 10

            ans = str(temp % 10) + ans

            i, j = i - 1, j - 1

        return "1" + ans if carry else ans 

# @lc code=end

