#
# @lc app=leetcode.cn id=101 lang=python3
#
# [101] 对称二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root: return False

        st = []
        st.append(root.left)
        st.append(root.right)

        while st:
            leftNode = st.pop()
            rightNode = st.pop()

            if not leftNode and not rightNode:
                continue
            elif not leftNode and rightNode:
                return False
            elif leftNode and not rightNode:
                return False
            elif leftNode.val != rightNode.val:
                return False

            st.append(leftNode.left)
            st.append(rightNode.right)
            st.append(leftNode.right)
            st.append(rightNode.left)

        return True

# @lc code=end

