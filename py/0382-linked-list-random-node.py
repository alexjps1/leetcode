"""
382. Linked List Random Node
by Alex JPS
2023-03-10

Solution With At Most Two Passes  
https://leetcode.com/problems/linked-list-random-node/
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import random

class Solution:

    def __init__(self, head: Optional[ListNode]):
        """Find length of list"""
        index = self.head = head
        self.len = 0
        while index:
            self.len += 1
            index = index.next
        
    def getRandom(self) -> int:
        """Select random number from list length,
        Return that node's value.
        """
        node = random.randrange(self.len)
        index = self.head
        while node > 0:
            index = index.next
            node -= 1
        return index.val


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
