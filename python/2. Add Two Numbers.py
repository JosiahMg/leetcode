"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.


Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]


Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/add-two-numbers
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


"""

from typing import List


class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    时间复杂的: O(n)
    空间复杂度: O(1)
    """
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = curr = ListNode(0)
        val = carry = 0
        while l1 or l2 or carry:
            val = carry
            if l1:
                val = l1.val + val
                l1 = l1.next
            if l2:
                val = l2.val + val
                l2 = l2.next
            
            carry, val = divmod(val, 10)
            curr.next = curr = ListNode(val)
        return head.next


    def printListNode(self, ln: ListNode):
        while ln:
            print(ln.val, end=' ')
            ln = ln.next

    def createListNode(self, l: List) -> ListNode:
        head = curr = ListNode(0)
        for data in l:
            curr.next = curr = ListNode(data)
        
        return head.next 



s = Solution()

l1 = [2, 4, 3]
l2 = [5, 6, 4]





res = s.addTwoNumbers(s.createListNode(l1), s.createListNode(l2))

s.printListNode(res)

