# https://leetcode.com/problems/swap-nodes-in-pairs/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        
        new_head = ListNode()
        new_head.next = head
        
        current_node = new_head
        
        while current_node.next is not None and current_node.next.next is not None:
            next_node = current_node.next
            next_next_node = current_node.next.next
            
            current_node.next = next_next_node
            next_node.next = next_next_node.next
            next_next_node.next = next_node
            current_node = next_node
            
        return new_head.next
        
        
        