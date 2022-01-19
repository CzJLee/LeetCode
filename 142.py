# https://leetcode.com/problems/linked-list-cycle-ii/submissions/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        seen = set()
        
        if head is None or head.next is None:
            return None
        
        while head.next:
            if head in seen:
                return head
            seen.add(head)
            head = head.next
            
        return None