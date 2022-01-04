# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
	def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
		# This is just simple addition. 
		sum_list_head = ListNode(None)
		sum_linked_list = sum_list_head
		quotient = 0

		while l1 or l2:
			a = 0 if l1 is None else l1.val
			b = 0 if l2 is None else l2.val

			quotient, remainder = divmod(quotient + a + b, 10)
			sum_linked_list.next = ListNode(remainder)
			sum_linked_list = sum_linked_list.next
			
			# Next node
			l1 = None if l1 is None else l1.next
			l2 = None if l2 is None else l2.next
		
		if quotient > 0:
			# Tack on a 1 if it carries over at the end
			sum_linked_list.next = ListNode(quotient)
		
		return sum_list_head.next