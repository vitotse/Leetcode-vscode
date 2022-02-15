/*
 * @lc app=leetcode.cn id=206 lang=swift
 *
 * [206] 反转链表
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public var val: Int
 *     public var next: ListNode?
 *     public init() { self.val = 0; self.next = nil; }
 *     public init(_ val: Int) { self.val = val; self.next = nil; }
 *     public init(_ val: Int, _ next: ListNode?) { self.val = val; self.next = next; }
 * }
 */

 public class ListNode {
      public var val: Int
      public var next: ListNode?
      public init() { self.val = 0; self.next = nil; }
      public init(_ val: Int) { self.val = val; self.next = nil; }
      public init(_ val: Int, _ next: ListNode?) { self.val = val; self.next = next; }  
}
class Solution {
    func reverseList(_ head: ListNode?) -> ListNode? {

        guard let head = head else {
            return nil
        }

        var nextNode = head
        var reverseNode = ListNode()

        while nextNode.next != nil {
            reverseNode = nextNode
            reverseNode.next = nextNode
            nextNode = nextNode.next!
            
        }

        return reverseNode
    }
}

var node2 = ListNode(2)
var node1 = ListNode(1, node2)
var headNode = ListNode(0, node1)

let solution = Solution()
let reverseNode = solution.reverseList(headNode)

if reverseNode != nil {
    print("node : \(reverseNode!)")
}

// @lc code=end

