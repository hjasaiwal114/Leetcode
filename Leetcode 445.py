"""
445. Add Two Number 2

You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1, num2 = 0, 0
        while l1 !=None:
            num1 = num1*10+l1.val
            l1 = l1.next
        
        while l2 != None:
            num2 = num2*10+l2.val
            l2 = l2.next

        dummylist = dummy = ListNode(0)

        ans = str(num1 + num2)
        for i in ans:
            dummy.next = ListNode(i)
            dummy = dummy.next
        
        return dummylist.next