"""
21. Merge Two Sorted Lists
by Alex JPS
2023-03-09

https://leetcode.com/problems/merge-two-sorted-lists
Simple 3-Step Solution with While Loop
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        # first comparison
        if list1 is None:
            return list2
        elif list2 is None:
            return list1
        elif list1.val <= list2.val:
            head = list1
            list1 = list1.next
        else:
            head = list2
            list2 = list2.next
        index = head

        # loop
        while list1 and list2:
            if list1.val <= list2.val:
                index.next = list1
                list1 = list1.next
                index = index.next
            else:
                index.next = list2
                list2 = list2.next
                index = index.next

        # tie up loose ends
        if list1 is None:
            index.next = list2
        else:
            index.next = list1
        return head
