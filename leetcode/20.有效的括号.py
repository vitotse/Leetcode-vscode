#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start

class Solution:
    def isValid(self, s: str) -> bool:
        signs = {')': '(', ']': '[', '}': '{'}

        stack = list()

        for ch in s:
            if ch == '(' or ch == '[' or ch == '{':
                stack.append(ch)

            else:
                if len(stack) == 0:
                    return False

                sign = signs[ch]

                if stack[-1] == sign:
                    stack.pop()
                else:
                    return False

        if len(stack) == 0:
            return True
        else:
            return False

# @lc code=end

