# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
	def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
		pointer_node = head
		for _ in range(n):
			pointer_node = pointer_node.next
		node_to_edit = head
		# At this point, the node to remove is n behind pointer
		if pointer_node is None:
			return head.next
		# Iterate pointer until the end of the list
		while pointer_node.next:
			pointer_node = pointer_node.next
			node_to_edit = node_to_edit.next
		# Change pointer
		node_to_edit.next = node_to_edit.next.next
		return head