#
# @lc app=leetcode.cn id=450 lang=python3
#
# [450] 删除二叉搜索树中的节点
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        if not root:
            return root
        if root.val == key:
            # 删除节点是叶子节点
            if not root.left and not root.right:
                return None
            # 删除节点只有左儿子，左儿子代替原节点
            elif root.left and not root.right:
                root = root.left
            # 删除节点只有右儿子，左儿子代替原节点
            elif root.right and not root.left:
                root = root.right
            elif root.left and root.right:
                # 既有左儿子，又有右儿子，把左子树接在右子树的最左节点的左边，右儿子代替原节点
                cur = root.right
                while cur.left:
                    cur = cur.left
                cur.left = root.left
                root = root.right
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        return root
            



# @lc code=end

