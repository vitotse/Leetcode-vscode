#
# @lc app=leetcode.cn id=150 lang=python3
#
# [150] 逆波兰表达式求值
#

# @lc code=start

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            print("tokens:"+token)
            if token == '+':
                stack.append(stack.pop() + stack.pop())
            elif token == '-':
                stack.append(-stack.pop() + stack.pop())
            elif token == '*':
                stack.append(stack.pop() * stack.pop())
            elif token == '/':
                stack.append(int(1/stack.pop()*stack.pop()))
            else:
                stack.append(int(token))
        
        return stack.pop()

# @lc code=end

