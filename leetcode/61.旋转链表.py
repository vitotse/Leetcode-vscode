#
# @lc app=leetcode.cn id=61 lang=python3
#
# [61] 旋转链表
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if not head:
            return None

        length = 0

        temp = head

        while temp.next:
            length += 1
            temp = temp.next
        # 头尾相连
        temp.next = head

        # 防止超过链表的长度
        k = k % (length + 1)

        for i in range(length - k + 1):
            temp = temp.next

        # 断开链表
        head = temp.next
        temp.next = None

        return head

# @lc code=end

