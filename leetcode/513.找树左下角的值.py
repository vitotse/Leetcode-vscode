#
# @lc app=leetcode.cn id=513 lang=python3
#
# [513] 找树左下角的值
#

# @lc code=start
# Definition for a binary tree node.

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        stack = deque([root])
        while stack:
            len_node = len(stack)
            left_node = stack[0]
            for _ in range(len_node):
                cur_node = stack.popleft()
                if cur_node.left: stack.append(cur_node.left)
                if cur_node.right: stack.append(cur_node.right)
        return left_node.val


# @lc code=end

