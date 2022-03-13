#
# @lc app=leetcode.cn id=148 lang=python3
#
# [148] 排序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next
        mid = slow.next 
        slow.next = None
        left = self.sortList(head)
        right = self.sortList(mid)
        c = d = ListNode(-1)
        while right and left:
            if left.val < right.val:
                c.next = left
                left = left.next
            else:
                c.next = right
                right = right.next
            c = c.next
        c.next = left if left else right
        return d.next
# @lc code=end

