# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
	def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
		# This is just simple addition. 
		sum_list = []
		quotient = 0

		node_1 = l1
		node_2 = l2

		while node_1 is not None or node_2 is not None:
			if node_1 is None:
				a = 0
			else: 
				a = node_1.val
			
			if node_2 is None:
				b = 0
			else: 
				b = node_2.val

			quotient, remainder = divmod(quotient + a + b, 10)
			sum_list.append(remainder)
			
			# Next node
			if node_1 is None:
				node_1 = None
			else:
				node_1 = node_1.next
			
			if node_2 is None:
				node_2 = None
			else:
				node_2 = node_2.next
		
		if quotient > 0:
			# Tack on a 1 if it carries over at the end
			sum_list.append(quotient)
		
		# Format output, create linked list
		# Reverse list
		sum_list.reverse()
		sum_linked_list = None
		for i in range(len(sum_list)):
			sum_linked_list = ListNode(val = sum_list[i], next = sum_linked_list)
		
		return sum_linked_list