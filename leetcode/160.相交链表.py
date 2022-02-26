#
# @lc app=leetcode.cn id=160 lang=python3
#
# [160] 相交链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        
        # 使用双指针
        a, b = headA, headB
        while a != b:
            # a 指针遍历完headA，遍历headB
            a = a.next if a else headB
            # b 指针遍历完headB，遍历headA
            b = b.next if b else headA

            # 如果没有相交，a、b等于none
        return a
# @lc code=end

