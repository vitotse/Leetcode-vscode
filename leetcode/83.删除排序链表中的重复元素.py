#
# @lc app=leetcode.cn id=83 lang=python3
#
# [83] 删除排序链表中的重复元素
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head

        dummy = ListNode()
        dummy.next = head
        pre = dummy.next

        while pre.next:
            if pre.val == pre.next.val:
                pre.next = pre.next.next
            else:
                pre = pre.next

        return dummy.next
# @lc code=end

